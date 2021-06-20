from django.contrib import admin
from ordenamiento.models import Parroquia, Barrio

# Register your models here.

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_parroquia')
    search_fields = ('nombre', 'tipo_parroquia')

# 1. Modelo (Parroquia) - 2.  Clase (ParroquiaAdmin)   
admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'viviendas', 'parques','edificios','parroquia')
    search_fields = ('nombre', 'parques')

# 1. Modelo (Barrio) - 2.  Clase (BarrioAdmin)
admin.site.register(Barrio, BarrioAdmin)