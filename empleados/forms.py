from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelChoiceField, ModelForm



class EmpleadosForm(ModelForm):
    
    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs ={
            'placeholder':'Ingrese nuevamente su contraseña',
            'required': 'required'
        }
    ))

    class Meta:
        model = Empleado
        fields = '__all__'
        

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2
    
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    