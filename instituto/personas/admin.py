from django.contrib import admin
from .models import Persona,Genero,Alumno,Producto

# Register your models here.
admin.site.register(Persona)
admin.site.register(Genero)
admin.site.register(Alumno)
admin.site.register(Producto)