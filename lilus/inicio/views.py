from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Coleccion, Foto
from unidecode import unidecode

###### información ######
def inicio(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True),
    }

    return render(request, 'inicio/inicio.html', context)

def contacto(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True),
    }
    return render(request, 'inicio/contacto.html', context)




def buscador(request):

    busqueda = request.GET.get('busqueda')
    if busqueda is '':
        busqueda = 'Todos'

    context = {
        'busqueda' : busqueda,
        'coleccion' : Coleccion.objects.filter(activa = True),
        'imagenes' : Foto.objects.filter(coleccion__nombre_real__icontains = unidecode(request.GET.get('busqueda'))),
    }

    return render(request, 'inicio/buscador.html', context)




def favoritos(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True),
    }
    return render(request, 'inicio/favoritos.html', context)

def coleccion(request, id_coleccion):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True),
        'coleccion_unica' : Coleccion.objects.get(id = id_coleccion),
        'imagen' : Foto.objects.filter(coleccion = id_coleccion),
    }
    return render(request, 'inicio/coleccion.html', context)


def evento(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True),
    }
    return render(request, 'inicio/evento.html', context)


def puntosDeVenta(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True),
    }
    return render(request, 'inicio/puntosDeVenta.html', context)
