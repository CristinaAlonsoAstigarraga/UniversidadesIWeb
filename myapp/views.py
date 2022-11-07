from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Universidad
from .models import Grado

# Create your views here.
#def paginaPrincipal(request):
 #   return HttpResponse("Hello, world!")

    
    #Por cada aplicación, se crea un nuevo file

def universidad(request, nombre):
    return HttpResponse("Consultando la empresa %s." % nombre)
    
def inicio(request):
    return HttpResponse("Listado universidades: ")

def listado_unis(request):
    universidad = Universidad.objects.all()   #Cogemos todas las unis de la clase Universidad
    clave = {'universidades': universidad}
    return render(request, 'universidades.html', clave)

def listado_grados(request):
    grado = Grado.objects.all()
    clave = {'grados': grado}
    return render(request, 'grados.html', clave)