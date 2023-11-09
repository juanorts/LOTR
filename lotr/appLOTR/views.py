
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Pelicula, Raza, Personaje

#   Devuelve el listado de razas
def index_razas(request):
    razas = get_list_or_404(Raza.objects.order_by('nombre'))
    context = {'razas': razas}
    return render(request, 'razas.html', context)

def show_raza(request, raza_id):
    raza = get_object_or_404(Raza, pk=raza_id)
    personajes = get_list_or_404(Personaje.objects.filter(raza_id=raza_id))
    context = {'raza': raza, 'personajes': personajes}
    return render(request, 'raza.html', context)

def index_personajes(request):
	personajes = get_list_or_404(Personaje.objects.order_by('nombre'))
	context = {'personajes' : personajes}
	return render(request, 'personajes.html', context)

#devuelve los detalles de un personaje
def show_personaje(request, personaje_id):
	personaje = get_object_or_404(Personaje, pk=personaje_id)
	context = { 'personaje': personaje}
	return render(request, 'personaje.html', context)

def index_peliculas(request):
	peliculas = get_list_or_404(Pelicula.objects.order_by('anyo'))
	context = {'lista_peliculas': peliculas }
	return render(request, 'peliculas.html', context)

def show_pelicula(request, pelicula_id):
	personajesPelicula = []
	pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
	personajes = get_list_or_404(Personaje)
	for p in personajes:
		for peli in p.pelicula.all():
			if peli.titulo == pelicula.titulo:
				personajesPelicula.append(p)
	context = {'pelicula': pelicula, 'personajes': personajesPelicula}
	return render(request, 'detailPelicula.html', context)

def index(request):
	personajes = get_list_or_404(Personaje.objects.order_by('raza'))
	context = {'lista_personajes': personajes }
	return render(request, 'index.html', context)