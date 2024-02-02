from django.contrib import admin

from partenaire.models import Partenaire, Reseaux


# Register your models here.

@admin.register(Partenaire)
class AdminMembre(admin.ModelAdmin):
    ...

@admin.register(Reseaux)
class AdminMembre(admin.ModelAdmin):
    ...