from django.shortcuts import render

from partenaire.models import Partenaire


# Create your views here.


def partenaire_index(request):

    list_partenaires = Partenaire.objects.all()
    context = {"list_partenaires": list_partenaires}

    return render(request, "partenaire/partenaire_index.html", context)