from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('buscador/', views.buscador, name='buscador'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('coleccion/<str:nombre_coleccion>/', views.coleccion, name='coleccion'),
    path('puntosDeVenta/', views.puntosDeVenta, name='puntosDeVenta'),
    path('blog/', views.blog, name='blog'),
    path('cookies/', views.cookies, name='cookies'),
    path('avisolegal/', views.avisoLegal, name='avisoLegal'),

    path('envioMail/', views.envioMail, name='envioMail'),
]
