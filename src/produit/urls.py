from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import produit_index, produit_detail, produit_index_par_categorie, produit_commander, mes_commande, \
    commande_detail

urlpatterns = [
    path('', produit_index, name="produit_index"),
    path('mes_commande', mes_commande, name="mes_commande"),
    path('commande_detail/<str:numero_de_commande>', commande_detail, name="commande_detail"),
    path('detail/<str:slug>', produit_detail, name="produit_detail"),
    path('categorie-par-categorie/<str:slug>', produit_index_par_categorie, name="produit_index_par_categorie"),
    path('commander/<str:slug>', produit_commander, name="produit_commander"),

]