from datetime import datetime
from django.db import models
from clientes.models import *
from django.core.exceptions import ValidationError
from causas.models import *
from empleados.models import *

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=True, blank=True)
    marca = models.CharField(max_length=20, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null=False, blank=False)
    unidad = models.CharField(max_length=10, blank=False, null=False)
    precio_unitario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    date = models.DateField(default=datetime.today())

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
        
class Servicio(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['id']

class Orden(models.Model):
    fecha_create = models.DateField(default=datetime.today())
    fecha = models.DateField(default=datetime.today())
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, null=False, blank=False, default='preventivo')
    lugar = models.CharField(max_length=50, null=False, blank=False, default='taller matriz')
    horometro = models.IntegerField(max_length=50, null=False, blank=False, default=0)
    estado = models.CharField(max_length=50, null=False, blank=False, default=0)
    aprobacion = models.BooleanField(default=False)
    observacion = models.TextField(max_length=250, null=True, blank=True)
    recomendacion = models.TextField(max_length=250, null=True, blank=True)
    tecnico = models.CharField(max_length=50, null=False, blank=False)
    recibe = models.CharField(max_length=50, null=False, blank=False)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
        ordering = ['id']
    
class detalleProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1, blank=False, null=False)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default=9999)
    
    def __str__(self):
        return self.producto
    
    class Meta:
        verbose_name = 'Detalle de Producto'
        verbose_name_plural = 'Detalle de Productos'
        ordering = ['id']

class DetalleServicio(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1, blank=False, null=False)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default=9999 )

    def __str__(self):
        return self.servicio

    class Meta:
        verbose_name = 'Detalle de servicio'
        verbose_name_plural = 'Detalle de servicios'
        ordering = ['id']

class DetalleCausas(models.Model):
    causa = models.ForeignKey(Causas, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default=9999 )
    
    def __str__(self):
        return self.causa
    
    class Meta:
        verbose_name = 'Detalle de Causa'
        verbose_name_plural = 'Detalle de Causas'
        ordering = ['id']
    
