from django.contrib import admin

from utilisateur.models import Utilisateur


# Register your models here.


@admin.register(Utilisateur)
class AdminUtilisateur(admin.ModelAdmin):
    ...