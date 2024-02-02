from django.urls import path

from .views import contact_index

urlpatterns = [
    path('', contact_index, name="contact_index"),

]