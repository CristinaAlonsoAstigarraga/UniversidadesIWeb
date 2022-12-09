from django.contrib import admin

from myapp.models import Universidad, Grado, Asignatura, Estudiante
# from .models import Question

from django.utils.html import format_html


# Creamos el modelo
@admin.register(Estudiante)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombreMayuscula', 'colorear', 'fechaInicio')
    ordering = ('nombre', '-fechaInicio')   # Ordenamos por nombre (ascendentes) primero y segundo por fechaa de inicio (descendente
    search_fields = ('dni', 'nombre')   # Panel búsqueda por dni o nombre
    list_per_page = 10
    #list_editable = ('nombre',) # Dejamos que el nombre se pueda modificar
    def nombreMayuscula(self, obj):
        return obj.nombre.upper()
    nombreMayuscula.short_description = "NOMBRE"

    def fechaIni(self, obj):
        return obj.fechaInicio
    fechaIni.short_description = "FECHA INICIO"


# Register your models here.
@admin.register(Universidad)
class UniversidadAdmin(admin.ModelAdmin):
    list_per_page = 10   # En vez de ver todas las universidades de golpe, ponemos diferentes páginas. En cada página se ven 10 universidades
    search_fields = ('nombre', 'ccaa')

@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'Duracion')
    search_fields = ('nombre',)
    ordering = ('nombre', 'duracion')
    list_per_page = 10


    

@admin.register(Asignatura)
class AsignarturaAdmin(admin.ModelAdmin):
    list_filter = ('creditos',)     # Podemos filtrar las asignaturas por el número de créditos
    search_fields = ('nombre',)
    #exclude = ('creditos',)     # Podemos ver el número de créidtos pero no editarlo
    list_per_page = 10
    # Se deja edita el número de créditos pulsando en 'advanced options - show'
    fieldsets =(
        (None, {
            'fields':('nombre','cod',)
        }), 
        ('Advanced options', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('creditos',) 
        })
    )

#admin.site.register(Estudiante)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']


# admin.site.register(Question, QuestionAdmin)

