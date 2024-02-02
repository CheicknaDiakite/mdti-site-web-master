from django import forms
from .models import Categorie


class CategorieForm(forms.Form):
    nom = forms.CharField(label="Nom", widget=forms.TextInput(attrs={'class': 'form-control'}))

