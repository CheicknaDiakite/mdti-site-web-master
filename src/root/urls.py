"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import root_index, administration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administration', administration, name="administration"), # pareil que admin/

    path('', root_index,name="root_index"),

    path('tinymce/', include('tinymce.urls')),
    path('produit/', include("produit.urls")),
    path('assistance', include("assistance.urls")),
    path('contact/', include("contact.urls")),
    path('equipe/', include("equipe.urls")),
    path('partenaire/', include("partenaire.urls")),
    path('service/', include("service.urls")),
    path('utilisateur/', include("utilisateur.urls")),
    path('presentation/', include("presentation.urls")),
    path('formations/', include("formation.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
