
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import Pelicula, Raza, Personaje
from .forms import PersonajeForm
from django.http import HttpResponseRedirect

#   Devuelve el listado de razas
def index_razas(request):
    razas = get_list_or_404(Raza.objects.order_by('nombre'))
    context = {'razas': razas}
    return render(request, 'razas.html', context)

def show_raza(request, raza_id):
    raza = get_object_or_404(Raza, pk=raza_id)
    personajes = raza.personaje_set.all()
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
		for peli in p.peliculas.all():
			if peli.titulo == pelicula.titulo:
				personajesPelicula.append(p)
	context = {'pelicula': pelicula, 'personajes': personajesPelicula}
	return render(request, 'pelicula.html', context)

def index(request):
	personajesFiltrados = Personaje.objects.raw('SELECT * FROM appLOTR_personaje GROUP BY raza_id')
	for p in personajesFiltrados:
		print(p.raza_id)
	context = {'lista_personajes': personajesFiltrados }
	return render(request, 'index.html', context)

def anyadirPersonaje(request):
	enviado = False
	if request.method == "POST":
		form = PersonajeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/formularioPersonajes?enviado=True')
	else:
		form = PersonajeForm
		if 'enviado' in request.GET:
			enviado = True
	return render(request, 'formularioPersonajes.html', {'form':form, 'enviado':enviado})

def modificarPersonaje(request, personaje_id):
	personaje = get_object_or_404(Personaje, pk=personaje_id)
	form = PersonajeForm(request.POST or None, request.FILES or None, instance=personaje)
	if form.is_valid():
			form.save()
			return redirect('personajes')
	context = { 'personaje': personaje, 'form': form}
	return render(request, 'modificarPersonaje.html', context)
