from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import *

urlpatterns = [
    path('producto',login_required(ListarProducto.as_view()), name='producto'),
    path('producto/create',login_required(CreateProducto.as_view()), name='producto_create'),
    path('producto/update/<int:pk>',login_required(ActualizarProducto.as_view()), name='producto_update'),
    path('producto/delete/<int:pk>',login_required(EliminarProducto.as_view()), name='producto_delete'),
    path('servicios',login_required(ListarServicio.as_view()), name='servicios'),
    path('servicios/create',login_required(CreateServicio.as_view()), name='servicios_create'),
    path('servicios/update/<int:pk>',login_required(ActualizarServicio.as_view()), name='servicios_update'),
    path('servicios/delete/<int:pk>',login_required(EliminarServicio.as_view()), name='servicios_delete'),
    path('categorias',login_required(CategoriaList.as_view()), name='categorias'),
    path('categorias/delete/<int:pk>',login_required(EliminarCategoria.as_view()), name='categorias_delete'),
    path('',login_required(ordenCreate.as_view()), name='orden_create'),
    path('ordenes',login_required(OrdenList.as_view()), name='ordenes'),
    path('ordenes/delete/<int:pk>',login_required(EliminarOrden.as_view()), name='orden_delete'),
    path('ordenes/update/<int:pk>',login_required(ordenUpdate.as_view()), name='orden_update'),
    path('ordenes/pdf/<int:pk>',login_required(OrdenPdfView.as_view()), name='orden_pdf'),
    
]
