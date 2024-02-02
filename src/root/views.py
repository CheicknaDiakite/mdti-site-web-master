from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from equipe.models import Membre
from formation.models import Formation
from partenaire.models import Partenaire
from presentation.models import Slider, Apropo
from produit.models import Produit
from service.models import Service


def administration(request):
    return redirect("/admin")

def index(request,):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
        'Contact Form',
        message,
        'settings.EMAIL_HOST_USER',
        [email,'example2@gmail.com','abcd@gmail.com'],
        fail_silently=False)
        return render(request, 'index.html')


def root_index(request):

    list_presentations = Slider.objects.all().order_by("-id")[:3]
    list_equipes = Membre.objects.all().order_by("-id")[:3]
    list_services = Service.objects.all().order_by("-id")[:3]
    list_produits = Produit.objects.all().order_by("-id")[:3]
    list_apropos = Apropo.objects.all().order_by("-id")
    list_partenaires = Partenaire.objects.all()
    all_formation = Formation.objects.all()[:3]
    context = {"list_partenaires": list_partenaires,
               "list_produits": list_produits,
               "list_equipes": list_equipes,
               "list_presentations": list_presentations,
               "list_apropos": list_apropos,
               "list_services": list_services,
               "all_formation": all_formation,
               }

    return render(request, "index.html", context)