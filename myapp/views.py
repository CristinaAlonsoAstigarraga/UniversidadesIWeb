from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Universidad
from .models import Grado
from .models import Estudiante
from .models import Asignatura


# Create your views here.
#def paginaPrincipal(request):
 #   return HttpResponse("Hello, world!")

    
    #Por cada aplicación, se crea un nuevo file

# def universidad(request, nombre):
#     return HttpResponse("Consultando la empresa %s." % nombre)
    
def inicio(request):
    return HttpResponse(request, 'inicio.html')

def listado_unis(request):
    universidad = Universidad.objects.all()   #Cogemos todas las unis de la clase Universidad
    clave = {'universidades': universidad}
    return render(request, 'universidades.html', clave)

def listado_grados(request):
    grado = Grado.objects.all()
    clave = {'grados': grado}
    return render(request, 'grados.html', clave)

def listado_estudiantes(request):
    estudiante = Estudiante.objects.all()
    clave = {'estudiantes': estudiante}
    return render(request, 'estudiantes.html', clave)

def listado_asignaturas(request):
    asignatura = Asignatura.objects.all()
    clave = {'asignaturas': asignatura}
    return render(request, 'asignaturas.html', clave)

def obtenerNumEstudiantes(request):
    estudiante = Estudiante.objects.all()
    total = len(estudiante)
    return total


# def obtenerNumEstudiantes(request, nombre):
#     grado = Grado.objects.get(Grado.universidad=nombre)
#     clave = {'grados': grado}
#     return total

# def filtrarUnisCCAA(request, ccaaFilt):
#     Grado.objects.filter(visible=True).filter(title__icontains = ccaaFilt)
