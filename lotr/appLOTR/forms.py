from django import forms
from django.forms import ModelForm
from .models import Personaje

#Crear un formulario para añadir personajes
class PersonajeForm(ModelForm):
    class Meta:
        model = Personaje    
        fields = ("raza", "peliculas", "nombre", "genero", "colorOjos", "colorPelo", "estatura", "imagen")
        labels = {
            'raza': 'Raza del Personaje',
            'peliculas': 'Peliculas en las que ha aparecido',
            'nombre': 'Nombre del Personaje',
            'genero': 'Genero del Personaje',
            'colorOjos': 'Color de ojos',
            'colorPelo': 'Color de pelo',
            'estatura': 'Estatura en cm',
            'imagen': 'Imagen'}

