from django.urls import path
from . import views
import myapp


urlpatterns = [
    path('hola', views.paginaPrincipal, name='index'),

    # ej: /miApp/
    path('', views.index, name='index'),

    # ej: /miApp/empresas/
    path('<str:nombre_empresa>/', views.empresa, name='empresa'),

    # ej: /miApp/empresas/5/
    path('empresas/<int:id_empresa>', views.actualizar, name='detalle'),

    # ej: /myapp/empresas/listadoNombre
    path('empresas/listadoempresas/', views.listadoEmpresas, name='listadoEmpresas'),

    # ej: /myapp/empresas/5
    path('empresas/detallesEmpresaID/<str:id_empresa>', views.detallesEmpresaID, name='detallesEmpresaID'),

    # ej: /myapp/empresas/nombreEmpresaCoincide/Samsu
    path('empresas/nombreEmpresaCoincide/<str:nombre_empresa>', views.nombreEmpresaCoincide, name='nombreEmpresaCoincide'),
]