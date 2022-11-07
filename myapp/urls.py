from django.urls import path
from . import views
import myapp


urlpatterns = [
    #path('hola', views.paginaPrincipal, name='index'),

    # ej: /myapp/universidad/
    #path('<str:nombre>/', views.universidad, name='universidad'),

    # ej: /myapp/inicio/
    #path('<str:>/', views.universidad, name='inicio'),

    # ej: 
    # /myapp/universidades/listadouniversidades/
    path('universidades/listadouniversidades/', views.listado_unis, name='listado_unis'),

    # /myapp/universidades/listadouniversidades/
    path('universidades/listadouniversidades/universidades.html', views.listado_unis, name='listado_unis'),

    # /myapp/universidades/listadogrados/
    path('universidades/listadouniversidades/grados.html', views.listado_grados, name='listado_grados')
]