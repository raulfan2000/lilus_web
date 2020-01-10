from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models
from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from PIL import Image
import uuid


# colecciones
class Coleccion(models.Model):
    class Meta:
        verbose_name = "Colección"
        verbose_name_plural = "Colecciones"
    # opciones de tipo de coleccion
    CHOICES = (('Evento', 'Evento'),('Comunion', 'Comunión'), ('Bautizo', 'Bautizo'), ('Verano', 'Verano'))
    # campos
    id = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    creacion = models.DateTimeField(auto_now_add=True, blank=True)
    nombre_real = models.CharField(max_length=32, default='')
    nombre = models.CharField(max_length=32, default='')
    tipo = models.CharField(max_length=32, choices=CHOICES, default='Evento')
    anyo = models.IntegerField(default=2020)
    activa = models.BooleanField(default=False)
    # nombre en bbdd
    def __str__ (self):
        return f'{str(self.nombre)}'

# fotos
class Foto(models.Model):
    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
    # campos
    id = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    creacion = models.DateTimeField(auto_now_add=True, blank=True)
    imagen = models.ImageField(default='default.jpg', upload_to='galeria_imagenes')
    # coleccion
    coleccion = models.ForeignKey(Coleccion, on_delete=models.SET_NULL, null=True)
    # guardar foto en la bbdd
    def save(self, force_insert=False, force_update=False, using=None):
        super().save()
        img1 = Image.open(self.imagen.path)
        if img1.height > 1300 or img1.width > 1300 :
            output_size = (1300,1300)
            img1.thumbnail((output_size), Image.ANTIALIAS)
            img1.save(self.imagen.path)
    def __str__ (self):
        return f'{str(self.coleccion)} {str(self.id)}'

# contacto
class Contacto(models.Model):
    class Meta:
        verbose_name = "Formulario de contacto"
        verbose_name_plural = "Formularios de contacto"
    # campos
    id = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    creacion = models.DateTimeField(auto_now_add=True, blank=True)
    nombre = models.CharField(max_length=32, default='')
    apellidos = models.CharField(max_length=120, default='')
    correo = models.CharField(max_length=120, default='')
    pais = models.CharField(max_length=120, default='')
    prefijo = models.CharField(max_length=120, default='')
    telefono = models.IntegerField(default=000000000)
    idioma = models.CharField(max_length=120, default='')
    mensaje = models.CharField(max_length=5000, default='')
    # nombre en bbdd
    def __str__ (self):
        return f'{str(self.nombre)}'
