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

    listaTotalUniversidad = []  ##la posicion 0 va a ser la universidad y todos sus grados
    universidad = Universidad.objects.all()   #Cogemos todas las unis de la clase Universidad
    listaGrados = []
    for u in universidad:
        grados = Grado.objects.filter(universidad = u)
        for g in grados:
            listaGrados.append(g)

    ##llegados a este punto tengo todas las universidades y todos los grados de cada una, pero separados

    for i in range(0, len(universidad)):
        tupla = (universidad[i], listaGrados[i])
        listaTotalUniversidad.append(tupla)


    clave = {'listaTotal': listaTotalUniversidad}
    return render(request, 'universidades.html', clave)

def listado_unis2(request):

    listaTotalUniversidad = []  ##la posicion 0 va a ser la universidad y todos sus grados
    universidad = Universidad.objects.all()   #Cogemos todas las unis de la clase Universidad
    listaEstudiantes = []
    for u in universidad:
        estudiantes = Estudiante.objects.filter(universidad = u)
        for e in estudiantes:
            listaEstudiantes.append(e)

    ##llegados a este punto tengo todas las universidades y todos los grados de cada una, pero separados

    for i in range(0, len(universidad)):
        tupla = (universidad[i], listaEstudiantes[i])
        listaTotalUniversidad.append(tupla)


    clave = {'listaTotal': listaTotalUniversidad}
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

def gradosUniversidad(request, nombreUniversidad):
    universidad = Universidad.objects.get(nombre = nombreUniversidad)
    grados = Grado.objects.filter(universidad = universidad)
    clave = {'grados': grados}
    return render(request, 'grados_uni.html', clave)


def estudiantesUniversidad(request, nombreUniversidad):
    universidad = Universidad.objects.get(nombre = nombreUniversidad)
    estudiantes = Estudiante.objects.filter(universidad = universidad)
    clave2 = {'estudiantes': estudiantes}
    return render(request, 'estudiantes.html', clave2)




# def obtenerNumEstudiantes(request, nombre):
#     grado = Grado.objects.get(Grado.universidad=nombre)
#     clave = {'grados': grado}
#     return total

# def filtrarUnisCCAA(request, ccaaFilt):
#     Grado.objects.filter(visible=True).filter(title__icontains = ccaaFilt)
