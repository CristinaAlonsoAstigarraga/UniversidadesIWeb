from django.urls import path
from . import views
import myapp


urlpatterns = [
    #path('hola', views.paginaPrincipal, name='index'),

    # ej: /miApp/universidad/
    path('<str:nombre>/', views.universidad, name='universidad'),
]