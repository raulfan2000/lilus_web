from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from unidecode import unidecode
from inicio.models import Coleccion, Foto
from django.db.models import Q

@login_required
def dashboard(request):
    context = {
        'coleccion': Coleccion.objects.filter(activa=True).order_by('-nombre'),
    }
    return render(request, 'clientes/dashboard.html', context)


@login_required
def coleccion(request, nombre_coleccion):
    context = {
        'coleccion': Coleccion.objects.all().order_by('-nombre'),
        'coleccion_unica': Coleccion.objects.get(nombre_real=nombre_coleccion),
        'imagen': Foto.objects.filter(coleccion__nombre_real=nombre_coleccion).order_by('nombre'),
    }
    return render(request, 'clientes/coleccion.html', context)

@login_required
def buscador(request):
    busqueda = request.GET.get('busqueda')
    if busqueda is '':
        busqueda = 'Todos'

    qset = (
        Q(coleccion__nombre_real__icontains=unidecode(request.GET.get('busqueda'))) |
        Q(nombre__icontains=unidecode(request.GET.get('busqueda')))
    )
    context = {
        'busqueda': busqueda,
        'coleccion': Coleccion.objects.filter(activa=True).order_by('-nombre'),
        'imagenes': Foto.objects.filter(qset, coleccion__activa=True).distinct(),
    }

    return render(request, 'clientes/buscador.html', context)
