from django.urls import path

from assistance.views import assistance_index, assistance

urlpatterns = [
    path('', assistance_index, name="assistance_index"),
    path('page', assistance, name="assistance"),

]