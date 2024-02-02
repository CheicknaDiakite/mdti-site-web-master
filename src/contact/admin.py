from django.contrib import admin

from contact.models import Contact


# Register your models here.

@admin.register(Contact)
class AdminMembre(admin.ModelAdmin):
    list_display = ["nom_prenom","sujet","email","numero","repondu"]
    list_filter = ["repondu"]

