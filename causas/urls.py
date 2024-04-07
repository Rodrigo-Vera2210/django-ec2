from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import *

urlpatterns = [
    path('',login_required(ListarCausas.as_view()), name='causas'),
    path('delete/<int:pk>',login_required(EliminarCausas.as_view()), name='causas_delete'),
]