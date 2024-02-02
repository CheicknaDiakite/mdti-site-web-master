import base64

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from root.settings import EMAIL_HOST_USER
from .models import Categorie, Formation, Client


# Create your views here.


def formation_categorie_index(request):

    all_cateogrie = Categorie.objects.all()
    all_formation = Formation.objects.all()
    context = {"all_cateogrie": all_cateogrie,
               "all_formation": all_formation,
            }
    return render(request, "formation/index.html", context=context)


def formation_detaille(request,slug):

    formation = Formation.objects.all().filter(slug=slug).first()
    return render(request,"formation/formation_detaille.html",context={"formation":formation})


def formation_inscription(request,slug):

    formation = Formation.objects.all().filter(slug=slug).first()
    utilisateur = request.user
    context = {"utilisateur":utilisateur, "formation":formation }


    if not request.user.is_authenticated:
        # base64_bytes = base64.b64encode(request.build_absolute_uri)
        # base64_string = base64_bytes.decode("ascii")

        sample_string_bytes = str(request.path).encode("ascii")

        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        messages.warning(request,"Connectez-vous pour vous inscrire")

        return redirect(reverse("connexion", kwargs={'next': base64_string}))

    if request.method == "POST":

        if Client.objects.all().filter(formation=formation,utilisateur=utilisateur).first():
            messages.error(request, "Vous êtes déjà inscrit à cette formation")
        else:
            new_client = Client(formation=formation,utilisateur=utilisateur)
            new_client.save()

            message = (f"Bonjour  {utilisateur.last_name} <br> "
                       f"Vous venez de vous inscrire a notre formation : <b>{formation.titre}</b> <br>"
                       f"Merci pour l'inscription")

            html_info = render_to_string("email/email_info.html", {"message": message})

            send_mail(
                "Demande d'Inscription de Formation",
                "",
                EMAIL_HOST_USER,
                recipient_list=[utilisateur.email],
                html_message=html_info)
            # TODO send mail
            messages.success(request,"Vous êtes inscrit")

        return redirect("formation_categorie_index")

    formation = Formation.objects.all().filter(slug=slug).first()
    context = {"utilisateur":request.user, "formation":formation }

    return render(request,"formation/inscription_formation.html",context=context)