from django.urls import path
from . import views
urlpatterns = [
    path('holamundo', views.holamundoCore, name='core'),
    path('', views.inicio, name='inicio'),
    path('acerca', views.acerca, name='acerca'),
    path('portafolio', views.portafolio, name='portafolio'),
    path('contacto', views.contacto, name='contacto'),
]

