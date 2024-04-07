from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import *

urlpatterns = [
    path('',login_required(ListarEmpleados.as_view()), name='empleado'),
    path('create',CreateEmpleado.as_view(), name='empleado_create'),
    path('update/<int:pk>',ActualizarEmpleado.as_view(), name='empleado_update'),
    path('delete/<int:pk>',login_required(EliminarEmpleado.as_view()), name='empleado_delete'),
]