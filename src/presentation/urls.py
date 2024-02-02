from django.urls import path

from .views import presentation_index

urlpatterns = [
    path('', presentation_index, name="presentation_index"),

]