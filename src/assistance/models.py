from django.db import models


# Create your models here.
class Rendezvous(models.Model):

    nom = models.CharField(max_length=255, verbose_name="Nom", blank=True)
    prenom = models.CharField(max_length=255, verbose_name="Prenom", blank=True)
    email = models.EmailField()
    numero = models.CharField(max_length=200, blank=True, null=True, verbose_name="Phone")
    sujet = models.CharField(max_length=300, verbose_name="Sujet", blank=True, null=True)
    date_rendezvous = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.nom
