from django.db import models

# Create your models here.

LIST_ = [
    ("facebook", "Facebook"),
    ("twitter", "X"),
]

class Specialiter(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Membre(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank=True, verbose_name="Image: 500x500")
    numero = models.CharField(max_length=30)
    specialite = models.ForeignKey(Specialiter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    @property
    def reseaus(self):
        return self.reseaux_set.all()


class Reseaux(models.Model):
    nom = models.CharField(max_length=255, choices=LIST_)
    url = models.URLField()
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        tmp_reseau = Reseaux.objects.all().filter(membre=self.membre,nom=self.nom).first()
        if tmp_reseau:
            tmp_reseau.delete()


        super().save()

