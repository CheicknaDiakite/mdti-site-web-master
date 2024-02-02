import base64
import random
import string

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from root.settings import EMAIL_HOST_USER
from utilisateur.models import Utilisateur, ResetPasswordCode


# Create your views here.


def connexion(request,next=None):

    if request.user.is_authenticated:
        return redirect(reverse("root_index"))

    if request.method == "POST":
        form_data = request.POST
        username = form_data.get("username")
        password = form_data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            messages.success(request, "Vous êtes connecter")
            login(request, user)
            if next:

                # base64_string = " R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA =="
                base64_bytes = next.encode("ascii")

                sample_string_bytes = base64.b64decode(base64_bytes)
                sample_string = sample_string_bytes.decode("ascii")
                # print(sample_string)
                return redirect(sample_string)

                # base64_bytes = next.encode("ascii")
                #
                # sample_string_bytes = base64.b64decode(base64_bytes)
                # sample_string = sample_string_bytes.decode("ascii")

            else:
                return redirect(reverse("root_index"))
        else:
            messages.error(request, "Mot de passe ou nom d'utilisateur incorrect")
            return render(request, "utilisateur/connexion.html",context={"message":"Mot de passe ou nom d'utilisateur incorrect"})

    return render(request,"utilisateur/connexion.html")

def inscription(request):

    if request.user.is_authenticated:
        return redirect(reverse("root_index"))

    if request.method == "POST":
        form_data = request.POST

        first_name = form_data.get("first_name")
        last_name = form_data.get("last_name")
        numero = form_data.get("numero")
        email = form_data.get("email")
        quartier = form_data.get("quartier")
        sexe = form_data.get("sexe")
        username = form_data.get("username")
        password = form_data.get("password")


        # verifier si le username est deja utiliser
        tmp_user_username = Utilisateur.objects.all().filter(username=username).first()
        tmp_user_email = Utilisateur.objects.all().filter(email=email).first()
        tmp_user_numero = Utilisateur.objects.all().filter(numero=numero).first()

        if tmp_user_username :
            messages.error(request,"Cet nom d'ulisateur est déjà utilisé")
        elif tmp_user_email:
            messages.error(request,"Cet email est déjà utilisé")
        elif tmp_user_numero:
            messages.error(request,"Cet numero est déjà utilisé")
        else:
            Utilisateur.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                numero=numero,
                email=email,
                quartier=quartier,
                sexe=sexe,
                username=username,
                password=password,
            )

            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, f"Bonjour {first_name} {last_name} <br>Merci de vous avoir inscrit sur notre site")

            html_ins = render_to_string("email/email_inscription.html", )

            send_mail(
                "Inscrption",
                "",
                EMAIL_HOST_USER
                ,
                recipient_list=[email],
                html_message=html_ins)
            # send mail


            return redirect(reverse("root_index"))

    #     Utilisateur.objects.create_user


    return render(request,"utilisateur/inscription.html")


def profile(request,modification=None):

    if modification:
        modification = True
    else:
        modification = False

    utilisateur = request.user

    if request.method == "POST":
        form = request.POST

        modifier = False

        last_name = form.get("last_name")
        if last_name != utilisateur.last_name:
            utilisateur.last_name = last_name
            utilisateur.save()
            modifier = True

        first_name = form.get("first_name")

        if first_name != utilisateur.first_name:
            utilisateur.first_name = first_name
            utilisateur.save()
            modifier = True

        numero = form.get("numero")
        if numero != utilisateur.numero:
            tmp_user = Utilisateur.objects.all().filter(numero=numero).first()
            if not tmp_user:
                utilisateur.numero = numero
                utilisateur.save()
                modifier = True
            else:
                messages.error(request, "Ce numéro est déjà utiliser")
                return redirect("profile")

        email = form.get("email")
        if email != utilisateur.email:
            tmp_user = Utilisateur.objects.all().filter(email=email).first()
            if not  tmp_user:
                utilisateur.email = email
                utilisateur.save()
                modifier = True
            else:
                messages.error(request,"Cet email est déjà utiliser")
                return redirect("profile")

        quartier = form.get("quartier")

        if quartier != utilisateur.quartier:
            utilisateur.quartier = quartier
            utilisateur.save()
            modifier = True

        sexe = form.get("sexe")

        if sexe != ""  and sexe != utilisateur.sexe:
            utilisateur.sexe = sexe
            utilisateur.save()
            modifier = True

        if modifier:
            messages.success(request, "Profile modifier")

        return redirect("profile")


    context = {"modification":modification,"utilisateur":utilisateur}
    return render(request,"utilisateur/profile.html",context=context)

def deconnexion(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecter")


    return redirect(reverse("root_index"))



def mot_de_passe_oublier(request):
    print("mot_de_passe_oublier")
    if request.method == "POST":
        form = request.POST
        username = form.get("username")
        email = form.get("email")

        tmp_user = Utilisateur.objects.all().filter(username=username, email=email).first()

        if not tmp_user:
            messages.error(request,"Utilisateur non trouvé")
            return redirect("root_index")

        sample_string_bytes = email.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        email_string = base64_bytes.decode("ascii")


        sample_string_bytes = username.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        username_string = base64_bytes.decode("ascii")


        code = "".join(random.choices(list(string.digits + string.ascii_uppercase), k=6))
        print(code)
        print(code)

        tmp_code = ResetPasswordCode.objects.all().filter(utilisateur=tmp_user)


        # desactiver tous les codes existant pour ce utilisateur
        for c in tmp_code:
            c.valide = False
            c.save()



        # trouver un code unique
        while ResetPasswordCode.objects.all().filter(code=code).first():
            code = "".join(random.choices(list(string.digits + string.ascii_uppercase + string.digits ), k=6))

        # enregistrer un nouveau code
        new_code = ResetPasswordCode(utilisateur=tmp_user,code=code)
        new_code.save()



        html_body = render_to_string("email/email_rest_password.html", context={
            "code":code,
        })

        send_mail(
            "Réinitialisation",
            "",
            EMAIL_HOST_USER
            ,
            recipient_list=[email],
            html_message=html_body)

        try:
            ...
            # send_mail(
            #     "Réinitialisation",
            #     "",
            #     EMAIL_HOST_USER
            #     ,
            #     recipient_list=[email],
            #     html_message=html_body
            # )
        except:
            ...

        messages.success(request,"Un code vous a été envoyer par email")
        return redirect("reset_password")

    return render(request,"utilisateur/mot_de_passe_oublier.html")


def reset_password(request):
    print("reset_password")

    if request.method == "POST":
        form = request.POST
        code = form.get("code")
        password = form.get("password")

        tmp_code = ResetPasswordCode.objects.all().filter(code=code).first()

        if tmp_code and tmp_code.valide:
            user = tmp_code.utilisateur
            user.set_password(password)
            user.save()
            tmp_code.delete()
            messages.success(request,"Votre mot de passe a été changer avec success")
            return redirect("connexion")
        else:
            messages.error(request,"Code invalide")


    return render(request,"utilisateur/reset_password.html")


