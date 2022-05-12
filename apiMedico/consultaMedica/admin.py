# Register your models here.
from django.contrib import admin
from .models import Medico, Paciente, FichaMedica

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(FichaMedica)