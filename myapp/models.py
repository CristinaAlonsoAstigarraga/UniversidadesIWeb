from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Universidad(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=12)
    ccaa = models.CharField(max_length=50)
    sistemaEducativo = models.CharField(max_length=50)  #Opciones: publica, privada
    
    def __str__(self):
        return self.nombre

class Grado(models.Model):
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE) #, related_name='grados'
    nombre = models.CharField(max_length=50)
    cod = models.CharField(max_length=12)
    duracion = models.IntegerField(default=4)

    def __str__(self):
        return self.nombre


class Asignatura(models.Model):
    grados = models.ForeignKey(Grado, on_delete=models.CASCADE) #Asiganturas que se ofrecen en cada grado
    nombre = models.CharField(max_length=50)
    cod = models.CharField(max_length=12)
    creditos = models.IntegerField(default=6)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    dni = models.CharField(max_length=9)
    fecha_nacimiento = models.DateField()
    # Es posible indicar un valor por defecto mediante 'default'
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    fechaInicio = models.DateField()

    def __str__(self):
        return self.nombre


