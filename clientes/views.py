from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
from control.models import *
from django.urls import reverse_lazy
from django.http import JsonResponse
import qrcode

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class ListarCliente(ListView):
    model = Cliente
    template_name = 'Cliente/index.html'
    context_object_name = 'clientes'
    
    def get(self, request,  *args, **kwargs):
        clientes = Cliente.objects.filter(nombres__contains = request.GET.get('search', ''))
        context = {
            'clientes': clientes
        }
        return render(request, 'Cliente/index.html', context)

class CreateCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/create.html'
    success_url = reverse_lazy('cliente')

class ActualizarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/actualizar.html'
    success_url = reverse_lazy('cliente')

class EliminarCliente(DeleteView):
    model = Cliente
    template_name = 'Control/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente')

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('cliente')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

class ListarEquipo(ListView):
    model = Equipo
    template_name = 'equipo/index.html'
    context_object_name = 'equipos'
    
    def get(self, request,  *args, **kwargs):
        equipos = Equipo.objects.filter(nombre__contains = request.GET.get('search', ''))
        context = {
            'equipos': equipos
        }
        return render(request, 'equipo/index.html', context)

class CreateEquipo(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/create.html'
    success_url = reverse_lazy('equipo')

class ActualizarEquipo(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/actualizar.html'
    success_url = reverse_lazy('equipo')

class EliminarEquipo(DeleteView):
    model = Equipo
    template_name = 'Control/equipo_confirm_delete.html'
    success_url = reverse_lazy('equipo')

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('equipo')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

class ListarHistorial(ListView):
    model = Equipo
    template_name = 'equipo/historial.html'
    

    def get_context_data(self, **kwargs):
        equipo = Equipo.objects.get(id = self.kwargs['pk'])
        ordenes = Orden.objects.filter(equipo = self.kwargs['pk'])
        for orden in ordenes:
            causas = DetalleCausas.objects.filter(orden_id = orden.id)
            orden.causa = causas[0].causa
        print(equipo.nombre)
        context = super().get_context_data(**kwargs)
        context = { 
            'equipo': equipo,
            'ordenes': ordenes
        }
        return context
    
    def post(self, request, *args, **kwargs):
        data = {}
        if request.POST['action'] == 'generarQR':
            try:
                input = request.POST['ruta']
                qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
                qr.add_data(input)
                qr.make(fit=True)
                img = qr.make_image(fill='black',black_color='white')
                img.save(f"static/img/qr_{request.POST['pk']}.png")
                data['error'] = ''
            except Exception as e:
                data['error'] = str(e)
        return JsonResponse(data)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs) 