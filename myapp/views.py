from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Universidad

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
    return render(request, 'lista_universidad.html', clave)
