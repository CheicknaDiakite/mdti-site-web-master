from django.shortcuts import render
from django.urls import path

from equipe.models import Membre


# Create your views here.


def equipe_index(request):

    list_equipes = Membre.objects.all()
    context = {"list_equipes": list_equipes}

    return render(request,"equipe/equipe_index.html", context)