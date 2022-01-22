from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('etudiants', getEtudiants, name='etudiants'),
    path('entreprises', getEntreprises, name='entreprises'),
    path('enseignants', getEnseignants, name='enseignants'),
    path('encadreurs', getEncadreurs, name='encadreurs'),
    path('data', data),
    path('stages', getStages, name='stages'),
    path('etudiants/add', addEtudiant, name='addEtudiant'),
    path('enseignants/add', addEnseignant, name='addEnseignant'),
    path('encadreurs/add', addEncadreur, name='addEncadreur'),
    path('entreprises/add', addEntreprise, name='addEntreprise'),
    path('stages/add', addStage, name='addStage'),
    path('etudiants/rm/<int:matricule>',deleteEtudiant,name='etudiantRm'),
    path('etudiants/<int:matricule>', setEtudiant, name='etudiant'),
    path('encadreurs/<int:id>', setEncadreur, name='encadreur'),
    path('encadreurs/rm/<int:id>', deleteEncadreur, name='encadreurRm'),
    path('entreprises/<int:id>', setEntreprise, name='entreprise'),
    path('entreprises/rm/<int:id>', deleteEntreprise, name='entrepriseRm'),
    path('enseignants/<int:matricule>', setEnseignant, name='enseignant'),
    path('enseignants/rm/<int:matriculeEns>', deleteEnseignant, name='enseignantRm'),
    path('stages/<int:id>', setStage, name='stage'),
    path('stages/rm/<int:id>', deleteStage, name='stageRm'),
    path('types', types, name='types')
]
