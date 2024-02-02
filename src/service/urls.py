from django.urls import path

from .views import service_index, service_detail

urlpatterns = [
    path('', service_index, name="service_index"),
path('detail/<str:slug>', service_detail, name="service_detail")
]