from statistics import mode
from django.db import models

# Create your models here.


class Etudiant(models.Model):
    choixAnnee = [('1CP', '1CP'), ('2CP', '2CP'), ('1CS', '1CS'),
                  ('2CS', '2CS'), ('3CS', '3CS')]
    matricule = models.PositiveBigIntegerField(primary_key=True)
    nomEtudiant = models.CharField(max_length=40)
    prenomEtudiant = models.CharField(max_length=30)
    dateNaiss = models.DateField()
    anneeEtudes = models.CharField(max_length=3, choices=choixAnnee)



class TypeStages(models.Model):
   
    désignation = models.CharField(max_length=30)
    obligatoire = models.BooleanField()
    nbrePageRapport = models.IntegerField()
    duréeEstimée = models.IntegerField()  
    debutPeriode = models.CharField(max_length=20)
    finPeriode = models.CharField(max_length=20)

  

class Entreprise(models.Model):
    nomEntreprise = models.CharField(max_length=40)
    secteur = models.CharField(max_length=40)
    adresseEntreprise = models.CharField(max_length=80)
    emailEntreprise = models.EmailField(null=True)
    telEntreprise = models.PositiveBigIntegerField(null=True)
    siteweb = models.CharField(max_length=60, null=True)




class Encadreur (models.Model):
    nomEncadreur = models.CharField(max_length=40)
    prenomEncadreur = models.CharField(max_length=30)
    poste = models.CharField(max_length=30, null=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

   


class Enseignant(models.Model):
    matriculeEns = models.PositiveBigIntegerField(primary_key=True)
    nomEnseignant = models.CharField(max_length=40)
    prenomEnseignant = models.CharField(max_length=30)
    grd = (('maître assistant B','maître assistant B'), ( 'maître assistant A','maître assistant A'), (
           'maître conférence B','maître conférence B'), ('maître conférence A','maître conférence A'), ( 'proffesseur','proffesseur'))
    grade = models.CharField(max_length=22, choices=grd)
    département = models.CharField(max_length=40)



class Stage (models.Model):
    nomProjet = models.CharField(max_length=60)
    objectifStage = models.TextField(max_length=100)
    annee = models.IntegerField()
    dateDeb = models.DateField()
    dureeReel = models.IntegerField()
    type = models.ForeignKey(TypeStages, on_delete=models.CASCADE)
    encadreur  = models.ForeignKey(Encadreur,on_delete=models.CASCADE,null=True)
    enseignant =  models.ForeignKey(Enseignant,on_delete=models.CASCADE,null=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    etudiants = models.ManyToManyField(Etudiant, related_name="stages")
    noteEvaluation = models.IntegerField( null=True)


