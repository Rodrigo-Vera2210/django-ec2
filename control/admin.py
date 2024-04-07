from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResourse(resources.ModelResource):
    class Meta:
        model = Categoria

class OrdenResourse(resources.ModelResource):
    class Meta:
        model = Orden

class ProductoResourse(resources.ModelResource):
    class Meta:
        model = Producto

class DetalleCausasResourse(resources.ModelResource):
    class Meta:
        model = DetalleCausas

class DetalleServicioResourse(resources.ModelResource):
    class Meta:
        model = DetalleServicio

class DetalleProductoResourse(resources.ModelResource):
    class Meta:
        model = detalleProducto

class ServicioResourse(resources.ModelResource):
    class Meta:
        model = Servicio

class ClienteResourse(resources.ModelResource):
    class Meta:
        model = Cliente

class EquipoResourse(resources.ModelResource):
    class Meta:
        model = Equipo

class CausasResourse(resources.ModelResource):
    class Meta:
        model = Causas

# Register your models here.

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre',)
    resource_class = CategoriaResourse

class OrdenAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id','cliente','fecha']
    list_display = ('id','cliente','equipo','total','fecha','tecnico','recibe')
    resource_class = OrdenResourse

class ProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','cantidad','unidad','precio_unitario')
    resource_class = ProductoResourse

class DetalleCausasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['orden']
    list_display = ('id','orden','causa')
    resource_class = DetalleCausasResourse

class DetalleServicioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id','orden','servicio','cantidad','precio','subtotal')
    resource_class = DetalleServicioResourse

class DetalleProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id','orden','producto','cantidad','precio','subtotal')
    resource_class = DetalleProductoResourse

class ServicioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','categoria','precio')
    resource_class = ServicioResourse

class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('id','nombres','c_id','email','direccion','telefono')
    resource_class = ClienteResourse

class EquipoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','cliente','nombre','modelo','marca','serie')
    resource_class = EquipoResourse

class CausasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre',)
    resource_class = CausasResourse

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(DetalleServicio, DetalleServicioAdmin)
admin.site.register(DetalleCausas, DetalleCausasAdmin)
admin.site.register(detalleProducto, DetalleProductoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Causas, CausasAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Equipo, EquipoAdmin)