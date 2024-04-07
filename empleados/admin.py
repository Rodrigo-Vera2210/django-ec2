from django.contrib import admin
from .models import *
# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','apellido','email','username','direccion','telefono')

admin.site.register(Empleado, EmpleadoAdmin)