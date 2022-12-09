from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.html import format_html


class Universidad(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=12)
    ccaa = models.CharField(max_length=50)
    sistemaEducativo = models.CharField(max_length=50)  #Opciones: publica, privada
    
    def __str__(self):
        return self.nombre

class Grado(models.Model):
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE , related_name='grados')
    nombre = models.CharField(max_length=50)
    cod = models.CharField(max_length=12)
    duracion = models.IntegerField(default=4)

    def __str__(self):
        texto = "{0} ({1})" 
        return texto.format(self.nombre, self.duracion)

    # Coloreamos las asignaturas con 4 creditoss o mas fecha de nacimiento de los estudiantes
    def Duracion(self):
        if self.duracion > 4: 
            return format_html('<span style="color: rgb(62, 186, 31);">{0}</span>'.format(self.duracion, self.nombre))
        else:
            return format_html('<span style="color: rgb(0, 0, 0);">{0}</span>'.format(self.duracion, self.nombre))



class Asignatura(models.Model):
    grados = models.ForeignKey(Grado, on_delete=models.CASCADE , related_name='asignaturas') #Asiganturas que se ofrecen en cada grado
    nombre = models.CharField(max_length=50)
    cod = models.CharField(max_length=12)
    creditos = models.IntegerField(default=6)

    def __str__(self):
        texto = "{0} ({1})"     # Mostramos el nombre de la asignatura y el número de créditos
        return texto.format(self.nombre, self.creditos)

    

class Estudiante(models.Model):
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE , related_name='estudiantes')
    nombre = models.CharField(max_length=40)
    dni = models.CharField(max_length=9)
    fecha_nacimiento = models.DateField()
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE,  related_name='estudiantes')
    fechaInicio = models.DateField()

    def __str__(self):
        return self.nombre

    # Coloreamos la fecha de nacimiento de los estudiantes
    def colorear(self):
        return format_html('<span style="color: rgb(62, 186, 31);">{0}</span>'.format(self.fecha_nacimiento))



# Cambio recomendable en el models 
# ingredientes = modelos.ManyToManyField(Ingrediente, related_name='pizzas2'
# Ingrediente.pizzas2.all  Te devuelve todas las pizzas con esos ingredientes.    #

