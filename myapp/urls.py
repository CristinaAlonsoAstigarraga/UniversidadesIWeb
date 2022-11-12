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

    # /myapp/inicio/
    #path('inicio/', views.inicio, name='inicio'),

    # /myapp/universidades/listadouniversidades/
    path('universidades/listadouniversidades/', views.listado_unis, name='listado_unis'),

    # /myapp/universidades/listadouniversidades/
    path('universidades/listadouniversidades/universidades.html', views.listado_unis, name='listado_unis'),

    # /myapp/universidades/listadogrados/
    path('universidades/listadouniversidades/grados.html', views.listado_grados, name='listado_grados'),

    # /myapp/universidades/listadoasignaturas/
    path('universidades/listadouniversidades/asignaturas.html', views.listado_asignaturas, name='listado_asignaturas'),

    # /myapp/universidades/obtenerNumEstudiantes
    #path('universidades/obtenerNumEstudiantes', views.obtenerNumEstudiantes, name='obtenerNumEstudiantes'),

    # /myapp/universidades/listadoestudiantes/
    path('universidades/listadouniversidades/estudiantes.html', views.listado_estudiantes, name='listado_estudiantes'), 

    path('universidades/grados/<str:nombreUniversidad>/', views.gradosUniversidad, name='gradosUniversidad'),

    path('universidades/estudiantes/<str:nombreUniversidad>/', views.estudiantesUniversidad, name='estudiantesUniversidad')
]


# Crear elemento tipo a "gradosuniversidad", que haga referencia (href) a un path que apunte a una vista nueva 
# que recibe como hiperparametro el nombre de la uni
# En la view pido los grados que coincidan con el nombre que he recibido en el hiperparametro que he puesto

# FALTA CREAR UNA URL QUE SEA LA QUE LLEVA DIRECTAMENTE A UN GRADO, DE AHI LA ASOCIAS CON EL HREF DEL ELEMENTO A.
# CUANDO CREES ESA URL TEN EN CUENTA QUE LE VAS A PASAR ALGO COMO UN ID, STRING O LO QUE SEA MEDIANTE EL <int:ID> 