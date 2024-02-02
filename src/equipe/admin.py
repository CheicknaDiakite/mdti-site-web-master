from django.contrib import admin

from equipe.models import Membre, Reseaux, Specialiter


# Register your models here.
# admin.site.register(Membre)
# admin.site.register(Reseaux)

@admin.register(Specialiter)
class AdminSpecialiter(admin.ModelAdmin):
    ...
@admin.register(Membre)
class AdminMembre(admin.ModelAdmin):
    list_display = ["nom", "prenom", "numero"]
    list_filter = ["specialite"]

@admin.register(Reseaux)
class AdminReseaux(admin.ModelAdmin):
    ...