from django.shortcuts import render
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