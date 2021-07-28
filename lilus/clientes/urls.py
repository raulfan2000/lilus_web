from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('coleccion/<str:nombre_coleccion>/', views.coleccion, name='coleccion_cliente'),
    path('buscador/', views.buscador, name='buscador_cliente'),
]
