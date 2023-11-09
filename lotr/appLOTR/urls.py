from django.urls import path
from . import views

urlpatterns = [
    path('razas/', views.index_razas, name='razas'),
    path('razas/<int:raza_id>', views.show_raza, name='raza'),
    path('personajes/', views.index_personajes, name='personajes'),
    path('personajes/<int:personaje_id>', views.show_personaje, name='personaje'),
]