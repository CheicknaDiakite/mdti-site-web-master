from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string

from assistance.models import Rendezvous
from root.settings import EMAIL_HOST_USER


# Create your views here.


def assistance_index(request):

    if request.method == "POST":
        form_data = request.POST

        nom = form_data.get("nom")
        prenom = form_data.get("prenom")
        numero = form_data.get("numero")
        email = form_data.get("email")
        sujet = form_data.get("sujet")
        message = form_data.get("message")
        date_rendezvous = form_data.get("date_rendezvous")

        new_rendezvous = Rendezvous(  nom=nom,
                                      prenom=prenom,
                                      date_rendezvous=date_rendezvous,
                                      message=message,
                                      email=email,
                                      sujet=sujet,
                                      numero=numero)

        new_rendezvous.save()

        message = f"Bonjour {nom} {prenom} <br> Votre demande de rendez-vous a bien été prise en compte"
        html_info = render_to_string("email/email_info.html", {"message": message})

        send_mail(
            "demande de rendez-vous",
            "",
            EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html_info)

        messages.success(request, "Votre demande de rendez-vous a bien été prise en compte")

        # TODO send rendez-vous

        context = {"message": "Message envoyer"}

        return  redirect("root_index")

    return  render(request,"assistance/assistance_index.html")

def assistance(request):
    ...
