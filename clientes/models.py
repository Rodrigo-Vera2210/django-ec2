from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    c_id = models.CharField(max_length=13, null=False, blank=False)
    email = models.EmailField(max_length=30)
    direccion = models.CharField(max_length=30, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    fecha_create = models.DateField(default=datetime.today())

    
    def vacio_validation(self):
        if self.nombre == '':
            raise ValidationError(' No existe el cliente')
        
    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class Equipo(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    serie = models.CharField(max_length=50, null=False, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['id']