from django.urls import path

from .views import connexion, inscription, profile, deconnexion, mot_de_passe_oublier, reset_password

urlpatterns = [
    path('connexion', connexion, name="connexion"),
    path('connexion/<str:next>', connexion, name="connexion"),
    path('inscription', inscription, name="inscription"),
    path('profile', profile, name="profile"),
    path('profile/<str:modification>', profile, name="profile_modification"),
    path('mot-de-passe-oublier', mot_de_passe_oublier, name="mot_de_passe_oublier"),
    path('reset-password', reset_password, name="reset_password"),
    path('deconnexion', deconnexion, name="deconnexion"),
]