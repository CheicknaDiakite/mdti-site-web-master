from django.db import models

# Create your models here.

class Contact(models.Model):
    nom_prenom = models.CharField(max_length=255)
    sujet = models.CharField(max_length=512)
    message = models.TextField()
    adresse = models.CharField(max_length=255)
    numero = models.IntegerField()
    email = models.EmailField()
    repondu = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_prenom
