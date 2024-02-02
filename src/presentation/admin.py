from django.contrib import admin

from presentation.models import Slider, Apropo


# Register your models here.

@admin.register(Slider)
class AdminImage(admin.ModelAdmin):
    ...

@admin.register(Apropo)
class AdminImage(admin.ModelAdmin):
    ...