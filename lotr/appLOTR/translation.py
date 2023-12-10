from modeltranslation.translator import TranslationOptions, register
from .models import Personaje, Pelicula, Raza

@register(Personaje)
class PersonajeTranslationOptions(TranslationOptions):
    fields = ("genero", "colorOjos", "colorPelo",)

@register(Pelicula)
class PeliculaTranslationOptions(TranslationOptions):
    fields = ("titulo", "genero")

@register(Raza)
class RazaTranslationOptions(TranslationOptions):
    fields = ("nombre", "actitud", "caracteristica", "longevidad", "tamanyo")