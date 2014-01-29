from django.forms import ModelForm
from django.db import models
from llibres.models import Genere, Titol, Llibre


class FormGenere(ModelForm):
    class Meta:
        model = Genere
        fields = ['nom']

class FormTitol(ModelForm):
    class Meta:
        model = Titol
        fields = ['titol','sinopsis','genere', 'imatge']

class FormLlibre(ModelForm):
    class Meta:
        model = Llibre
        fields = ['idioma', 'isbn', 'edicio', 'editorial', 'titol', 'propietari', 'estat']