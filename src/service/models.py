from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


# Create your models here.

class Service(models.Model):
    nom = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = HTMLField()
    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    def _get_unique_slug(self):
        slug = slugify(self.nom)
        unique_slug = slug
        num = 1
        while Service.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()