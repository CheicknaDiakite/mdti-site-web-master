from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

from utilisateur.models import Utilisateur


# Create your models here.

class Categorie(models.Model):
    slug = models.SlugField(editable=False, unique=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    def _get_unique_slug(self):
        slug = slugify(self.nom)
        unique_slug = slug
        num = 1
        while Categorie.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, unique=True)
    reference = models.SlugField()

    prix = models.IntegerField()
    description = HTMLField()
    image_couverture = models.ImageField(null=True, blank=True, verbose_name="Image: 1200x700")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    def _get_unique_slug(self):
        slug = slugify(self.nom)
        unique_slug = slug
        num = 1
        while Produit.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

class Image(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, verbose_name="Image: 1200x700")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Document(models.Model):
    nom = models.CharField(max_length=255)
    document = models.FileField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    numero_de_commande = models.CharField(max_length=255)
    prix = models.FloatField()
    quantite = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    message = models.TextField()
    traiter = models.BooleanField(default=False)
    create_ajout = models.DateTimeField(null=True)
    create_traitement = models.DateTimeField(null=True)


    def __str__(self):
        return self.numero_de_commande


    @property
    def prix_total(self):
        return self.prix * self.quantite