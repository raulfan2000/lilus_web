from django import forms
from .models import Contacto

class formularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = {
            'nombre',
            'apellidos',
            'correo',
            'pais',
            'prefijo',
            'telefono',
            'idioma',
            'mensaje',
        }
