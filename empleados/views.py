import json
from django.core.serializers import serialize
from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse, JsonResponse

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class ListarEmpleados(ListView):
    model = Empleado
    template_name = 'empleados/index.html'
    context_object_name = 'empleados'
    
    def get(self, request,  *args, **kwargs):
        empleados = Empleado.object.filter(nombre__contains = request.GET.get('search', ''))
        context = {
            'empleados': empleados
        }
        return render(request, 'empleados/index.html', context)

class CreateEmpleado(CreateView):
    model = Empleado
    form_class = EmpleadosForm
    template_name = 'empleados/create.html'
    success_url = reverse_lazy('empleado')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name,{'form':form})
        print(form.cleaned_data.get('groups'))
        nuevo_empleado = Empleado(
            username = form.cleaned_data.get('username'),
            nombre = form.cleaned_data.get('nombre'),
            apellido = form.cleaned_data.get('apellido'),
            email = form.cleaned_data.get('email'),
            direccion = form.cleaned_data.get('direccion'),
            c_id = form.cleaned_data.get('c_id'),
            telefono = form.cleaned_data.get('telefono'),
        )
        groups = form.cleaned_data.get('groups')
        nuevo_empleado.set_password(form.cleaned_data.get('password1'))
        nuevo_empleado.save()
        for g in groups:
            nuevo_empleado.groups.add(g)
        return redirect('empleado')
    
class ActualizarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadosForm
    template_name = 'empleados/actualizar.html'
    success_url = reverse_lazy('empleado')

class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'Control/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado')

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('empleado')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

