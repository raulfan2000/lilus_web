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
    path('cookies/', views.cookies, name='cookies'),
    path('avisolegal/', views.avisoLegal, name='avisoLegal'),
    path('envioMail/', views.envioMail, name='envioMail'),
    path('login/', auth_views.LoginView.as_view(template_name='inicio/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]
 