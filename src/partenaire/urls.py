from django.urls import path

from .views import partenaire_index

urlpatterns = [
    path('', partenaire_index, name="partenaire_index"),

]