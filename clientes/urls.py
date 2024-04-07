from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import *

urlpatterns = [
    path('',login_required(ListarCliente.as_view()), name='cliente'),
    path('create',login_required(CreateCliente.as_view()), name='cliente_create'),
    path('update/<int:pk>',login_required(ActualizarCliente.as_view()), name='cliente_update'),
    path('delete/<int:pk>',login_required(EliminarCliente.as_view()), name='cliente_delete'),
    path('equipos/',login_required(ListarEquipo.as_view()), name='equipo'),
    path('equipos/create',login_required(CreateEquipo.as_view()), name='equipo_create'),
    path('equipos/update/<int:pk>',login_required(ActualizarEquipo.as_view()), name='equipo_update'),
    path('equipos/delete/<int:pk>',login_required(EliminarEquipo.as_view()), name='equipo_delete'),
    path('equipos/historial/<int:pk>',login_required(ListarHistorial.as_view()), name='equipo_historial'),
]