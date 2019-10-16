from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def inicio(request):
    return render(request, 'inicio/inicio.html')
def contacto(request):
    return render(request, 'inicio/contacto.html')

def comunion2019(request):
    return render(request, 'inicio/comunion2019.html')

def comunion2018(request):
    return render(request, 'inicio/comunion2018.html')

def verano2019(request):
    return render(request, 'inicio/verano2019.html')

def verano2018(request):
    return render(request, 'inicio/verano2018.html')

def bautizo(request):
    return render(request, 'inicio/bautizo.html')

def eventoValencia2019(request):
    return render(request, 'inicio/eventoValencia2019.html')
