from django.forms import ModelForm
from .models import *

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'