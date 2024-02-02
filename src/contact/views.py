from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from contact.models import Contact


# Create your views here.

def contact_index(request):


    if request.method == "POST" :
        form_data = request.POST
        print(form_data)

        nom_prenom = form_data.get("nom_prenom")
        email = form_data.get("email")
        sujet = form_data.get("sujet")
        message = form_data.get("message")
        adresse = form_data.get("adresse")
        numero = form_data.get("numero")



        new_contact = Contact(nom_prenom=nom_prenom,
                              message=message,
                              adresse=adresse,
                              email=email,
                              sujet=sujet,
                              numero=numero)

        new_contact.save()

        message = (f"Merci {nom_prenom} <br>"
                   f"Nous avons reussi votre message")

        html_info = render_to_string("email/email_info.html", {"message": message})

        send_mail(
            sujet,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html_info)

        messages.success(request, "Votre message a bien été envoyer")

        # TODO send mail

        return redirect("root_index")



    return render(request,"contact/contact_index.html")