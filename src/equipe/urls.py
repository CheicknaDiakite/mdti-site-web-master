from django.urls import path

from equipe.views import equipe_index

urlpatterns = [
    path('', equipe_index, name="equipe_index"),

]