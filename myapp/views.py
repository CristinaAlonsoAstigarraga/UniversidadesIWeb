from django.shortcuts import render
from django.http import HttpResponse
from .models import Universidad

# Create your views here.
#def paginaPrincipal(request):
 #   return HttpResponse("Hello, world!")

    
    #Por cada aplicación, se crea un nuevo file

def universidad(request, nombre):
    return HttpResponse("Consultando la empresa %s." % nombre)
    
