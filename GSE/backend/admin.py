from django.contrib import admin
from .models import Etudiant,Stage, TypeStages

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nomEtudiant', 'prenomEtudiant','anneeEtudes')

class typeStagesAdmin(admin.ModelAdmin):
    list_display = ('désignation','obligatoire','nbrePageRapport','duréeEstimée','debutPeriode','finPeriode')

class StageAdmin(admin.ModelAdmin):
    list_display = ('nomProjet','dateDeb')

admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(TypeStages,typeStagesAdmin)