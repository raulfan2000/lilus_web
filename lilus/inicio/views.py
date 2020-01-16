from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Coleccion, Foto
from unidecode import unidecode
from .forms import formularioContacto
from .mail import contactoMail

###### información ######
def inicio(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
    }

    return render(request, 'inicio/inicio.html', context)

def contacto(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
    }
    return render(request, 'inicio/contacto.html', context)


def envioMail(request):
    if request.method == 'POST':
        formulario = formularioContacto(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre = formulario.cleaned_data['nombre']
            apellidos = formulario.cleaned_data['apellidos']
            correo = formulario.cleaned_data['correo']
            pais = formulario.cleaned_data['pais']
            prefijo = formulario.cleaned_data['prefijo']
            telefono = formulario.cleaned_data['telefono']
            idioma = formulario.cleaned_data['idioma']
            mensaje = formulario.cleaned_data['mensaje']
            contactoMail({
                'nombre': nombre,
                'apellidos': apellidos,
                'correo': correo,
                'pais': pais,
                'prefijo': prefijo,
                'telefono': telefono,
                'idioma' : idioma,
                'mensaje': mensaje,
                'to': correo,
            }).send()
            messages.success(request, f'Formulario recibido correctamente.')
            return redirect('contacto')
        else:
            messages.error(request, f'Formulario no válido, intentalo de nuevo.')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, f'Formulario no válido, intentalo de nuevo.')
        return redirect(request.META.get('HTTP_REFERER'))



def buscador(request):
    busqueda = request.GET.get('busqueda')
    if busqueda is '':
        busqueda = 'Todos'

    context = {
        'busqueda' : busqueda,
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
        'imagenes' : Foto.objects.filter(coleccion__nombre_real__icontains = unidecode(request.GET.get('busqueda')), coleccion__activa = True),
    }

    return render(request, 'inicio/buscador.html', context)


def favoritos(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
    }
    return render(request, 'inicio/favoritos.html', context)


def coleccion(request, id_coleccion):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
        'coleccion_unica' : Coleccion.objects.get(id = id_coleccion),
        'imagen' : Foto.objects.filter(coleccion = id_coleccion).order_by('-creacion'),
    }
    return render(request, 'inicio/coleccion.html', context)


def blog(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
    }
    return render(request, 'inicio/blog.html', context)


def cookies(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
    }
    return render(request, 'inicio/cookies.html', context)


def avisoLegal(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
    }
    return render(request, 'inicio/privacidad.html', context)


def puntosDeVenta(request):
    context = {
        'coleccion' : Coleccion.objects.filter(activa = True).order_by('-nombre'),
    }
    return render(request, 'inicio/puntosDeVenta.html', context)
