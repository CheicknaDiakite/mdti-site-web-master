import base64
import random
import string
from django.contrib import messages
from django.core.mail import send_mail

from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from produit.forms import CategorieForm
from produit.models import Produit, Categorie, Image, Commande
from root.settings import EMAIL_HOST_USER


# Create your views here.
def produit_index(request):

    list_produits = Produit.objects.all()
    context = {"list_produits": list_produits}

    return render(request, "produit/produit_index.html", context)

def produit_index_par_categorie(request,slug):


    categorie = Categorie.objects.all().filter(slug = slug).first()
    if categorie:
        list_produits = Produit.objects.all().filter(categorie=categorie)

        context = {"list_produits": list_produits}

        return render(request, "produit/produit_index.html", context)
    else:
        ...

def produit_commander(request,slug):

    if not request.user.is_authenticated:
        # base64_bytes = base64.b64encode(request.build_absolute_uri)
        # base64_string = base64_bytes.decode("ascii")

        sample_string_bytes = str(request.path).encode("ascii")

        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")



        return redirect(reverse("connexion", kwargs={'next':base64_string}))

    if request.method == "POST":
        user_from_database = request.user

        form_data = request.POST
        slug = form_data.get("slug")
        quantite = form_data.get("quantite")
        message = form_data.get("message")
        produit_from_database = Produit.objects.all().filter(slug=slug).first()
        #
        # lettre_maj = string.ascii_uppercase
        # chiffre = string.digits

        numero_de_commande = "".join(random.choices(list(string.digits + string.ascii_uppercase),k=8))

        while Commande.objects.all().filter(numero_de_commande=numero_de_commande).first() :
            numero_de_commande = "".join(random.choices(list(string.digits + string.ascii_uppercase), k=8))


        new_commande = Commande(numero_de_commande=numero_de_commande,
                                prix=produit_from_database.prix,
                                quantite=quantite,
                                utilisateur=user_from_database,
                                produit=produit_from_database,
                                message=message
                                )
        new_commande.save()

        message = (f"Vous avez fait une commande de produit: {produit_from_database} <br>"
                   f"Le numero de commande est : <b> {numero_de_commande} </b>")

        html_info = render_to_string("email/email_info.html", {"message": message})

        send_mail(
            "Demande de produit",
            "",
            EMAIL_HOST_USER,
            recipient_list=[user_from_database.email],
            html_message=html_info)


        # TODO send mai to admin

        messages.success(request,"Votre commande a bien été effectuer")

        return redirect('produit_index')

    produit_from_database = Produit.objects.all().filter(slug=slug).first()

    return render(request, "produit/commander.html",context={"produit": produit_from_database})

def creer(request):
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']

            return redirect('index')
        else:
            return render(request, 'cat.html', {'form': form})
    else:
        form = CategorieForm()
        return render(request, 'cat.html', {'form': form})

def produit_detail(request, slug):

    list_produit = get_object_or_404(Produit, slug = slug)
    list_image = Image.objects.all()
    context = {"produit": list_produit,
               "list_images": list_image,
               }


    return render(request, "produit/produit_detail.html", context)

def mes_commande(request, ):

    utilisateur = request.user
    commandes = utilisateur.commande_set.all()



    context = {"commandes": commandes}

    return render(request, "produit/mes_commande.html", context)

def commande_detail(request, numero_de_commande):

    # commande = get_object_or_404(Commande, numero_de_commande=numero_de_commande)
    commande = Commande.objects.all().filter(numero_de_commande=numero_de_commande).first()

    context = {"commande": commande}

    return render(request, "produit/commande_detail.html", context)
