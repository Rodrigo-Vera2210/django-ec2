from django.forms import ModelForm
from .models import *

class CausasForm(ModelForm):
    class Meta:
        model = Causas
        fields = '__all__'