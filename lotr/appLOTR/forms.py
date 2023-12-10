from django import forms
from django.forms import ModelForm
from .models import Personaje
from django.utils.translation import gettext_lazy as _

#Crear un formulario para añadir personajes
class PersonajeForm(ModelForm):
    class Meta:
        model = Personaje    
        fields = ("raza", "peliculas", "nombre", "genero", "colorOjos", "colorPelo", "estatura", "imagen")
        labels = {
            'raza': _('Raza del Personaje'),
            'peliculas': _('Peliculas en las que ha aparecido'),
            'nombre': _('Nombre del Personaje'),
            'genero': _('Genero del Personaje'),
            'colorOjos': _('Color de ojos'),
            'colorPelo': _('Color de pelo'),
            'estatura': _('Estatura en cm'),
            'imagen': _('Imagen')}