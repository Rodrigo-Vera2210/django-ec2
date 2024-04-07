from django.forms import *
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class OrdenForm(ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class DetalleServicioForm(ModelForm):
    class Meta:
        model = DetalleServicio
        fields = '__all__'

class DetalleProducto(ModelForm):
    class Meta:
        model = detalleProducto
        fields = '__all__'