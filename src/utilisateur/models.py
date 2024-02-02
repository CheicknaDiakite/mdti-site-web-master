from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class Utilisateur(AbstractUser):

    email = models.EmailField(unique=True)
    numero = models.CharField(max_length=200, blank=True, null=True)
    sexe = models.CharField(max_length=30, verbose_name="Genre", blank=True, null=True)
    quartier = models.CharField(max_length=300, verbose_name="Quartier / ville", blank=True, null=True)
    travail = models.CharField(max_length=300,  blank=True, null=True)


class ResetPasswordCode(models.Model):
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    valide = models.BooleanField(default=True)