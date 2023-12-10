from django.contrib import admin
from .models import Personaje, Pelicula, Raza
from modeltranslation.admin import TranslationAdmin

@admin.register(Personaje)
class PersonajeAdmin(TranslationAdmin):
    list_display = ("nombre", )

@admin.register(Pelicula)
class PeliculaAdmin(TranslationAdmin):
    list_display = ("titulo", )

@admin.register(Raza)
class RazaAdmin(TranslationAdmin):
    list_display = ("nombre", )