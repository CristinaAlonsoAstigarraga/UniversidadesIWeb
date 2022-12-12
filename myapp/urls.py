from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import myapp


urlpatterns = [


    #PATHS - PARA LAS VISTAS BASADAS EN CLASES
    path('universidades/listadouniversidades/', views.show_universidades.as_view(), name='show_universidades'),
    
    path('inicio/', views.inicio.as_view(), name='inicio'),
    path('inicio/index/', views.inicio.as_view(), name='inicioI'),



    path('inicio/universidades/', views.show_universidades.as_view(), name='show_universidades'), #VentanaUniversidades - muestra el listado
    path('inicio/grados/', views.show_grados.as_view(), name='show_grados'),
    path('inicio/asignaturas/', views.show_asignaturas.as_view(), name='show_asignaturas'),
    path('inicio/estudiantes/', views.show_estudiantes.as_view(), name='show_estudiantes'),
    path('universidades/grados/<int:pk>/', views.gradosUniversidad.as_view(), name='gradosUniversidad'),
    # path('estudiantes/grados/<int:pk>/', views.gradoEstudiante.as_view(), name='gradoEstudiante'),
    path('universidades/asignaturas/<int:pk>/', views.asignaturasGrado.as_view(), name='asignaturasGrado'),
    path('universidades/estudiantes/<int:pk>/', views.estudiantesUniversidad.as_view(), name='estudiantesUniversidad'),
    path('universidades/estudiantesGrado/<int:pk>/', views.gradosUniversidadEstudiantes.as_view(), name='gradosUniEstudiantes'),
    # /myapp/universidades/estudiantes/<str:NombreUniversidad>/
    # path('universidades/estudiantes/<str:nombreUniversidad>/', views.estudiantesUniversidad, name='estudiantesUniversidad'),
    path('universidades/listadouniversidades/asignaturas/<str:nombreGrado>', views.estudiGrado, name='estudiantesUniversidad11'),   #NO FUNCIONA

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)