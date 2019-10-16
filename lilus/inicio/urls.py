from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('comunion2019', views.comunion2019, name='comunion2019'),
    path('comunion2018', views.comunion2018, name='comunion2018'),
    path('verano2019', views.verano2019, name='verano2019'),
    path('verano2018', views.verano2018, name='verano2018'),
    path('bautizo', views.bautizo, name='bautizo'),
    path('valencia2019', views.eventoValencia2019, name='eventoValencia2019'),
]
