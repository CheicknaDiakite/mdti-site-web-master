from django.contrib import admin

from service.models import Service


# Register your models here.

@admin.register(Service)
class AdminImage(admin.ModelAdmin):
    list_display = ["nom"]