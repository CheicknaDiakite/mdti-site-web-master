from django.contrib import admin

from produit.models import Produit, Categorie, Image, Document, Commande


# Register your models here.

# admin.site.register(Produit)
# admin.site.register(Categorie)
# admin.site.register(Image)

@admin.register(Produit)
class AdminProduit(admin.ModelAdmin):
    list_display = ["nom", "prix"]
    list_filter = ["categorie"]

@admin.register(Categorie)
class AdminCategorie(admin.ModelAdmin):
    list_display = ["nom"]

@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ["nom"]


@admin.register(Document)
class AdminImage(admin.ModelAdmin):
    list_display = ["nom"]

@admin.register(Commande)
class AdminUtilisateur(admin.ModelAdmin):
    list_display = ["numero_de_commande", "quantite", "prix", "utilisateur"]
    list_filter = ["traiter"]



