from django.contrib import admin
from .models import Sede, AmbienteFormacion, Instructor


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')
    ordering = ('nombre',)


@admin.register(AmbienteFormacion)
class AmbienteFormacionAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_aula',
        'capacidad_maxima',
        'sede'
    )
    list_filter = ('sede',)
    search_fields = ('codigo_aula', 'sede__nombre')
    ordering = ('codigo_aula',)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        'documento_identidad',
        'nombres',
        'apellidos',
        'correo_institucional'
    )
    search_fields = (
        'documento_identidad',
        'nombres',
        'apellidos',
        'correo_institucional'
    )
    filter_horizontal = ('ambientes',)
    ordering = ('apellidos', 'nombres')