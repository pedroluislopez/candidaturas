from django.contrib import admin
from candidatos.models import Candidato


# Register your models here.
class CandidatoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'apellidos', 'imagen', 'email']}),
        ('Datos personales', {'fields': ['nif', 'telefono']}),
        ('Candidatura', {'fields': ['secretario', 'consejo', 'biografia', 'motivacion', 'youtube', 'activo']}),
    ]
    list_display = ('nombre', 'apellidos', 'email', 'secretario', 'consejo', 'activo')
    list_filter = ['secretario', 'consejo']
    seach_fields = ['nombre', 'apellidos', 'email']
    
admin.site.register(Candidato, CandidatoAdmin)
