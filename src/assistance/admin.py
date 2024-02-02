from django.contrib import admin

from assistance.models import Rendezvous


# Register your models here.
@admin.register(Rendezvous)
class AdminMembre(admin.ModelAdmin):
    ...