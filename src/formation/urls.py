from django.urls import path

from .views import formation_categorie_index, formation_detaille, formation_inscription

urlpatterns = [
    path('', formation_categorie_index, name="formation_categorie_index"),
    path('detaille/<str:slug>', formation_detaille, name="formation_detaille"),
    path('inscription/<str:slug>', formation_inscription, name="formation_inscription"),

]