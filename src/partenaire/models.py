from django.db import models
from tinymce.models import HTMLField

LIST_ = [
    ("facebook", "Facebook"),
    ("twitter", "X"),
]

# Create your models here.
class Partenaire(models.Model):
    nom = models.CharField(max_length=255)
    description = HTMLField()
    photo = models.ImageField(null=True, blank=True, verbose_name="Image 500x500 ")
    site_web = models.URLField(null=True, blank=True)
    numero = models.IntegerField()

    def __str__(self):
        return self.nom

    @property
    def reseaus(self):
        return self.reseaux_set.all()

class Reseaux(models.Model):
    nom = models.CharField(max_length=255, choices=LIST_)
    url = models.URLField()
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom