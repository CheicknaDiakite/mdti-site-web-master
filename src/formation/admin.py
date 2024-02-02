from django.contrib import admin

from .models import Client, Formation, Categorie


# Register your models here.


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ["utilisateur","formation"]
    list_filter = ["formation"]


@admin.register(Formation)
class AdminFormation(admin.ModelAdmin):
    list_display = ["titre","date_debut","date_fin"]
    list_filter = ["categorie"]

@admin.register(Categorie)
class AdminCategorie(admin.ModelAdmin):
    ...

