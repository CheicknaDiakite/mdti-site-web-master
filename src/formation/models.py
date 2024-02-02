import time

from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

from utilisateur.models import Utilisateur


# Create your models here.



class Categorie(models.Model):
    titre = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(editable=False,blank=True)
    image = models.ImageField(upload_to=f"{time.time()}")
    description = models.TextField(max_length=500, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def _get_unique_slug(self):
        slug = slugify(self.titre)
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

class Formation(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    titre = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(editable=False,blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    image = models.ImageField()
    cour_description = models.TextField(max_length=100, default='')
    description = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre + " (Nombre de clients  " + str(len(self.client_set.all())) + " )"


    def _get_unique_slug(self):
        slug = slugify(self.titre)
        unique_slug = slug
        num = 1
        while Formation.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Client(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.utilisateur.first_name
