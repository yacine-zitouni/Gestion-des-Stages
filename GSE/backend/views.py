from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import render, redirect
from django.db.models import Q


def data(request):
    x = list(Stage.objects.order_by('annee').values_list('annee',flat=True).distinct())
    y = []
    for d in x : 
        y.append( Stage.objects.filter(annee=d).count())
    return JsonResponse({'x': x,'y':y})

def home(request):
    etudiants = Etudiant.objects.count()
    stages = Stage.objects.order_by('entreprise')
    nbStages = stages.count()

    
    encadreurs = Encadreur.objects.count()
    entreprises = Entreprise.objects.count()
    enseignants = Enseignant.objects.count()
    types = TypeStages.objects.count()
    return render(request, "index.html", {"types": types,
                   "enseignants": enseignants, "etudiants": etudiants, "data":stages, "stages": nbStages, "encadreurs": encadreurs, "entreprises": entreprises})


def types(request):
    types = TypeStages.objects.all()
    return render(request, "get/typeStages.html", {"data": types})


def getEntreprises(request):
    if 'recherche' in request.GET:
        cle = request.GET.get('recherche')
        entreprises = Entreprise.objects.filter(nomEntreprise__contains=cle)
    else:
        entreprises = Entreprise.objects.all()
    return render(request, "get/entreprises.html", {"data": entreprises})


def getStages(request):
    if 'recherche' in request.GET:
        cle = request.GET.get('recherche')
        stages = Stage.objects.filter(nomProjet__contains=cle)
    else:
        stages = Stage.objects.all()
    return render(request, "get/stages.html", {"data": stages})


def getEncadreurs(request):
    if 'recherche' in request.GET:
        cle = request.GET.get('recherche')
        encadreurs = Encadreur.objects.filter(
            Q(nomEncadreur__contains=cle) | Q(prenomEncadreur__contains=cle))
    else:
        encadreurs = Encadreur.objects.all()

    return render(request, "get/encadreurs.html", {"data": encadreurs})


def getEnseignants(request):
    if 'recherche' in request.GET:
        cle = request.GET.get('recherche')
        enseignants = Enseignant.objects.filter(nomEnseignant__contains=cle).union(Enseignant.objects.filter(
            prenomEnseignant__contains=cle)).union(Enseignant.objects.filter(département__contains=cle))
    else:
        enseignants = Enseignant.objects.all()
    return render(request, "get/enseignants.html", {"data": enseignants})


def getEtudiants(request):
    if 'recherche' in request.GET:
        cle = request.GET.get('recherche')
        etudiants = Etudiant.objects.filter(
            Q(nomEtudiant__contains=cle) | Q(prenomEtudiant__contains=cle))
    else:
        etudiants = Etudiant.objects.all()
    return render(request, "get/etudiants.html", {"data": etudiants})


def addEnseignant(request):
    if request.method == 'POST':
        mat = request.POST.get('mat')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        grade = request.POST.get('grade')
        département = request.POST.get('dep')
        et = Enseignant(matriculeEns=mat, nomEnseignant=nom,
                        prenomEnseignant=prenom, grade=grade, département=département)
        et.save()

        return redirect('enseignants')

    return render(request, "add/addEnseignant.html")


def addEncadreur(request):
    msg=''
    ent=Entreprise.objects.all()
    if request.method == 'POST':
        entreprise = Entreprise.objects.get(
            pk=request.POST.get('ent'))
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        poste = request.POST.get('poste')
        en = Encadreur(nomEncadreur=nom, prenomEncadreur=prenom,
                       entreprise=entreprise, poste=poste)
        en.save()
        redirect('encadreurs')
        msg = "Encadreur ajoutée avec succès "
    return render(request, "add/addEncadreur.html", {"msg": msg,"entreprises":ent})


def addEntreprise(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        secteur = request.POST.get('secteur')
        email = request.POST.get('email')
        adresse = request.POST.get('adr')
        tel = request.POST.get('tel')
        siteweb = request.POST.get('siteweb')
        en = Entreprise(nomEntreprise=nom, secteur=secteur, adresseEntreprise=adresse,
                        emailEntreprise=email, telEntreprise=tel, siteweb=siteweb)
        en.save()
        return redirect('entreprises')

    return render(request, "add/addEntreprise.html")


def addEtudiant(request):
    msg = ''

    if request.method == 'POST' or request.method == 'UPDATE':
        mat = request.POST.get('mat')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        dateNaiss = request.POST.get('dateNaiss')
        annee = request.POST.get('annee')
        et = Etudiant(matricule=mat, nomEtudiant=nom,
                      prenomEtudiant=prenom, dateNaiss=dateNaiss, anneeEtudes=annee)
        et.save()
        msg = 'Etudiant ajouté avec succées '
        redirect('get/etudiants')

    return render(request, "add/addEtudiant.html", {"msg": msg})


def addStage(request, id=None):
    enseignants = Enseignant.objects.all()
    etudiants = Etudiant.objects.all()
    encadreurs = Encadreur.objects.all()
    entreprises = Entreprise.objects.all()
    types = TypeStages.objects.all()
    if request.method == 'POST':
        et = request.POST.getlist('etudiant')
        et = Etudiant.objects.filter(pk__in=et)
        nom = request.POST.get('nom')
        obj = request.POST.get('obj')
        annee = request.POST.get('annee')
        date = request.POST.get('date')
        duree = request.POST.get('duree')
        typ = TypeStages.objects.get(pk=request.POST.get('type'))
        ens = Enseignant.objects.get(pk=request.POST.get('ens'))  # enseignant
        enc = Encadreur.objects.get(pk=request.POST.get('enc'))  # encadreur
        ent = Entreprise.objects.get(pk=request.POST.get('ent'))  # entreprise
        note = request.POST.get('note')
        st = Stage(id=None, nomProjet=nom, objectifStage=obj, annee=annee,
                   noteEvaluation=note,
                   dateDeb=date, dureeReel=duree, type=typ, encadreur=enc, entreprise=ent, enseignant=ens)
        st.save()
        st.etudiants.set(et)
        st.save()
        return redirect("stages")

    return render(request, "add/addStage.html", {
        "enseignants": enseignants,
        "encadreurs": encadreurs,
        "entreprises": entreprises,
        "types": types,
        "etudiants": etudiants,

    })


# update and get

def setEtudiant(request, matricule):
    try:
        if request.method == 'GET':
            etudiant = Etudiant.objects.get(pk=matricule)
            return render(request, "set/etudiant.html", {"data": etudiant})
        if request.method == 'POST':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            dateNaiss = request.POST.get('dateNaiss')
            annee = request.POST.get('annee')
            et = Etudiant(matricule, nomEtudiant=nom,
                          prenomEtudiant=prenom, dateNaiss=dateNaiss, anneeEtudes=annee)
            et.save()
            return redirect('etudiants')
    except:
        return render(request, "error-404.html")


def setEncadreur(request, id):
    try:
        entreprises = Entreprise.objects.all()

        if request.method == 'GET':
            encadreur = Encadreur.objects.get(pk=id)
            return render(request, "set/encadreur.html", {"data": encadreur, "entreprises": entreprises})
        if request.method == 'POST':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            poste = request.POST.get('poste')
            ent = Entreprise.objects.get(pk=request.POST.get('ent'))
            en = Encadreur(id, nomEncadreur=nom,
                           prenomEncadreur=prenom, poste=poste, entreprise=ent)
            en.save()
            return redirect('encadreurs')
    except:
        return render(request, "error-404.html")


def setEntreprise(request, id):
    try:

        if request.method == 'GET':
            entreprise = Entreprise.objects.get(pk=id)
            return render(request, "set/entreprise.html", {"data": entreprise})
        if request.method == 'POST':
            nom = request.POST.get('nom')
            secteur = request.POST.get('secteur')
            email = request.POST.get('email')
            adresse = request.POST.get('adr')
            tel = request.POST.get('tel')
            siteweb = request.POST.get('siteweb')
            ent = Entreprise(id, nomEntreprise=nom, secteur=secteur, adresseEntreprise=adresse,
                             emailEntreprise=email, telEntreprise=tel, siteweb=siteweb)
            ent.save()
            return redirect('entreprises')
    except:
        return render(request, "error-404.html")


def setStage(request, id):
    try:
        stage = Stage.objects.get(pk=id)
        if request.method == 'POST':
            et = request.POST.getlist('etudiant')
            et = Etudiant.objects.filter(pk__in=et)
            nom = request.POST.get('nom')
            obj = request.POST.get('obj')
            annee = request.POST.get('annee')
            date = request.POST.get('date')
            duree = request.POST.get('duree')
            typ = TypeStages.objects.get(pk=request.POST.get('type'))
            ens = Enseignant.objects.get(
                pk=request.POST.get('ens'))  # enseignant
            enc = Encadreur.objects.get(
                pk=request.POST.get('enc'))  # encadreur
            ent = Entreprise.objects.get(
                pk=request.POST.get('ent'))  # entreprise
            note = request.POST.get('note')
            st = Stage(id=id, nomProjet=nom, objectifStage=obj, annee=annee,
                       noteEvaluation=note,
                       dateDeb=date, dureeReel=duree, type=typ, encadreur=enc, entreprise=ent, enseignant=ens)
            st.save()
            st.etudiants.set(et)
            st.save()
            return redirect("stages")
        return render(request, "set/stage.html", {"data": stage})
    except:
        return render(request, "error-404.html")


def setEnseignant(request, matricule):
    try:
        enseignant = Enseignant.objects.get(pk=matricule)
        if request.method == 'POST':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            grade = request.POST.get('grade')
            département = request.POST.get('dep')
            et = Enseignant(matriculeEns=matricule, nomEnseignant=nom,
                            prenomEnseignant=prenom, grade=grade, département=département)
            et.save()
            return redirect('enseignants')
        return render(request, "set/enseignant.html", {"data": enseignant})
    except:
        return render(request, "error-404.html")

def deleteEtudiant(request,matricule):
    
    try:
       et =  Etudiant.objects.get(pk=matricule).delete()
       etudiants= Etudiant.objects.all()
       return render(request, "get/etudiants.html", {"data": etudiants})
    except:
        pass
        


def deleteEncadreur(request,id):
    
    try:
       et =  Encadreur.objects.get(pk=id).delete()
       encadreurs= Encadreur.objects.all()
       return render(request, "get/encadreurs.html", {"data": encadreurs})
    except:
        pass



def deleteEntreprise(request,id):
    
    try:
       et =  Entreprise.objects.get(pk=id).delete()
       entreprises= Entreprise.objects.all()
       return render(request, "get/entreprises.html", {"data": entreprises})
    except:
        pass

def deleteEnseignant(request,matriculeEns):
    
    try:
       et =  Enseignant.objects.get(pk=matriculeEns).delete()
       enseignants= Enseignant.objects.all()
       return render(request, "get/enseignants.html", {"data": enseignants})
    except:
        pass

def deleteStage(request,id):
    
    try:
       et =  Stage.objects.get(pk=id).delete()
       Stages= Stage.objects.all()
       return render(request, "get/stages.html", {"data": Stages})
    except:
        pass
        

