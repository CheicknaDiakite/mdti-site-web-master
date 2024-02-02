from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class Slider(models.Model):
    nom = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank=True, verbose_name="Image: 1920x1080")
    description = HTMLField()
    courte_description = models.TextField()

    def __str__(self):
        return self.nom

    # @property
    # def courte_description(self):
    #     return self.description[:25]

class Apropo(models.Model):
    titre = models.CharField(max_length=255)
    description = HTMLField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()

    def __str__(self):
        return self.titre