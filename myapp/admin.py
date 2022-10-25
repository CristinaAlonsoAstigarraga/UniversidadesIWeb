from django.contrib import admin

from myapp.models import Universidad, Grado, Asignatura, Estudiante

# Register your models here.
admin.site.register(Universidad)
admin.site.register(Grado)
admin.site.register(Asignatura)
admin.site.register(Estudiante)