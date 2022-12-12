from urllib import request
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Universidad
from .models import Grado
from .models import Estudiante
from .models import Asignatura
from django.utils.translation import gettext as _




#VISTAS BASADAS EN CLASES

class inicio(ListView):
    model = Universidad
    template_name = 'index.html'

#Listado universidades:
class show_universidades(ListView):
    model = Universidad
    template_name = 'universidades.html'  #Relacionado con la carpeta templates


#Listado grados:
class show_grados(ListView):
    model = Grado
    template_name = 'grados_uni.html'

#Listado asignaturas:
class show_asignaturas(ListView):
    model = Asignatura
    template_name = 'asignaturas.html'


#Listado estudiantes:
class show_estudiantes(ListView):
    model = Estudiante
    template_name = 'estudiantes.html'


""" #Info detallada de una universidad
class infoUni(DetailView):
    model = Universidad
    template_name = 'universidades.html'





#Info detallada de un grado
class infoGrado(DetailView):
    model = Grado
    template_name = 'grados_uni.html'





#Info detallada de una asignatura
class infoAsignatura(DetailView):
    model = Asignatura
    template_name = 'asignaturas.html'



#Info detallada de un estudiante
class infoEstudiatne(DetailView):
    model = Estudiante
    template_name = 'estudiantes.html'

 """
#VISTAS BASADAS EN FUNCIONES

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

def listado_unis3(request):

    listaTotalGrado = []  ##la posicion 0 va a ser la universidad y todos sus grados
    grado = Grado.objects.all()   #Cogemos todas las unis de la clase Universidad
    listaAsignaturas = []
    for g in grado:
        asignaturas = Asignatura.objects.filter(grado = g)
        for a in asignaturas:
            listaAsignaturas.append(a)

    ##llegados a este punto tengo todas las universidades y todos los grados de cada una, pero separados

    for i in range(0, len(grado)):
        tupla = (grado[i], listaAsignaturas[i])
        listaTotalGrado.append(tupla)

    clave = {'listaTotal': listaTotalGrado}
    return render(request, 'grados.html', clave)


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

class gradosUniversidad(DetailView):
    model = Universidad
    template_name = 'gradoUnico.html'

class estudiantesUniversidad(DetailView):
    model = Universidad
    template_name = 'estudianteUnico.html'

class gradosUniversidadEstudiantes(DetailView):
    model = Grado
    template_name = 'estudiantes.html'

class asignaturasGrado(DetailView):
    model = Grado
    template_name = 'asignaturaUnica.html'

class gradoEstudiante(DetailView):
    model = Grado
    template_name = "gradoUnico.html"

def estudiGrado(request, nombreGrado):
    grado = Grado.objects.get(nombre = nombreGrado)
    asignaturas = Asignatura.objects.filter(grados  = grado)
    clave3 = {'asignaturas': asignaturas}
    return render(request, 'asignaturas.html', clave3)

""" 

class show_universidades(DetailView):
    model = Universidad
    template_name = 'universidad.html'  #Relacionado con la carpeta templates """


