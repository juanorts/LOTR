from django.urls import path
from . import views

urlpatterns = [
    path('razas/', views.index_razas, name='razas'),
    path('razas/<int:raza_id>', views.show_raza, name='raza'),
    path('personajes/', views.index_personajes, name='personajes'),
    path('personajes/<int:personaje_id>', views.show_personaje, name='personaje'),
    path('', views.index, name='index'),
    path('peliculas/', views.index_peliculas, name='peliculas'),
    path('peliculas/<int:pelicula_id>/', views.show_pelicula, name='detailPelicula'),
    path('peliculas/<int:pelicula_id>/personajes', views.index_personajes, name='personajes')
 ]