import json
from django.core.serializers import serialize
from django.db import IntegrityError
from django.urls import reverse_lazy
from asyncio.windows_events import NULL
from typing import Any, Dict
from django.contrib import messages
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from clientes.models import *
from clientes.forms import *
from django.views.generic import *
from django.template.loader import get_template
from weasyprint import HTML
from inventario import settings


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class ListarProducto(ListView):
    model = Producto
    template_name = 'producto/index.html'
    context_object_name = 'productos'
    
    def get(self, request,  *args, **kwargs):
        productos = Producto.objects.filter(nombre__contains = request.GET.get('search', ''))
        context = {
            'productos': productos
        }
        return render(request, 'producto/index.html', context)

class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/create.html'
    success_url = reverse_lazy('producto')

class ActualizarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/actualizar.html'
    success_url = reverse_lazy('producto')

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'Control/producto_confirm_delete.html'
    success_url = reverse_lazy('producto')

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('producto')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

class ListarServicio(ListView):
    model = Servicio
    template_name = 'servicio/index.html'
    context_object_name = 'servicios'
    
    def get(self, request,  *args, **kwargs):
        servicios = Servicio.objects.filter(nombre__contains = request.GET.get('search', ''))
        context = {
            'servicios': servicios
        }
        return render(request, 'servicio/index.html', context)

class CreateServicio(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio/create.html'
    success_url = reverse_lazy('servicios')

class ActualizarServicio(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio/actualizar.html'
    success_url = reverse_lazy('servicios')

class EliminarServicio(DeleteView):
    model = Servicio
    template_name = 'Control/servicio_confirm_delete.html'
    success_url = reverse_lazy('servicios')
    
    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('servicios')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

class CategoriaList(ListView):
    template_name = "categoria/index.html"
    form_class = CategoriaForm
    model = Categoria
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        return context

    def get(self, request, letter = NULL, *args, **kwargs):
        if is_ajax(request = request):
            categorias = Categoria.objects.all()
            data = serialize('json', categorias)
            return JsonResponse(data,safe=False)
        else:
            if letter != NULL:
                categorias = Categoria.objects.filter(nombre__istartswith=letter)
            else:
                categorias = Categoria.objects.filter(nombre__contains = request.GET.get('search', ''))
            form = CategoriaForm()
            context = {
                'categorias': categorias,
                'form':form
            }
            return render(request, 'categoria/index.html', context)
    
    def post(self, request, *args, **kwargs):
        data = {"nombre" : str(request.POST['nombre'])}
        try:
            form = CategoriaForm(data)
            if form.is_valid:
                form.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

def categoria_create(request, letter = NULL):
    data = {}
    try:
        if request.method == 'GET':
            if letter != NULL:
                categorias = Categoria.objects.filter(nombre__istartswith=letter)
            else:
                categorias = Categoria.objects.filter(nombre__contains = request.GET.get('search', ''))
            context = {
                'categorias': categorias
            }
            return render(request, 'categoria/index.html', context)    
    
        if request.method == 'POST':
            form = CategoriaForm(request.POST)
            if form.is_valid:
                form.save()
            return redirect('categorias')
    except Exception as e:
        data['error'] = str(e)
        return JsonResponse(data)

class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'Control/categoria_confirm_delete.html'
    success_url = reverse_lazy('categorias')

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('categorias')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

class ordenCreate(LoginRequiredMixin,CreateView):
    model =  Orden
    form_class = OrdenForm
    template_name = 'orden/create'
    
    def get(self, request, *args, **kwargs):
        form = OrdenForm()
        context ={
            'form': form,
            'cliente2': Cliente.objects.all(),
            'servicios2': Servicio.objects.all(),
            'productos2': Producto.objects.all(),
            'causas2': Causas.objects.all(),
            'empleados': Empleado.object.all()
        }
        return render(request, 'orden/create.html',context)

    def post(self, request, *args, **kwargs):       
        data = {}
        
        if request.POST['action'] == 'search-cliente':
            try:
                equiposNombres = []
                equiposId = []
                cliente = Cliente.objects.get(id = str(request.POST['nombre']))
                equipos = Equipo.objects.filter(cliente_id = str(request.POST['nombre']))
                for equipo in equipos:
                    equiposNombres.append(equipo.nombre)
                    equiposId.append(equipo.id)
                data = {
                    'nombres': cliente.nombres,
                    'id': cliente.id,
                    'error': '',
                    'equiposN': equiposNombres,
                    'equiposI': equiposId 
                }
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
        if request.POST['action'] == 'search-equipo':
            try:
                equipo = Equipo.objects.get(nombre = str(request.POST['nombre']))
                print(equipo.nombre)
                data = {
                    'nombre': equipo.nombre,
                    'id': equipo.id,
                    'modelo': equipo.modelo,
                    'marca': equipo.marca,
                    'serie': equipo.serie,
                    'error': '',
                }
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
        if request.POST['action'] == 'search-causa':
            try:
                causa = Causas.objects.get(id = str(request.POST['nombre']))
                data = {
                    'causa': causa.id,
                    'nombre': causa.nombre,
                    'error': ''
                }
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
        if request.POST['action'] == 'search-servicio':
            try:
                servicio = Servicio.objects.get(id = str(request.POST['nombre']))
                data = {
                    'servicio': servicio.id,
                    'nombre': servicio.nombre,
                    'categoria': str(servicio.categoria),
                    'cantidad': 1,
                    'precio': servicio.precio,
                    'subtotal': servicio.precio,
                    'error': ''
                }
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
        if request.POST['action'] == 'search-producto':
            try:
                producto = Producto.objects.get(id = str(request.POST['nombre']))
                data = {
                    'producto': producto.id,
                    'nombre': producto.nombre,
                    'cantidadMax': producto.cantidad,
                    'cantidad': 1,
                    'precio': producto.precio_unitario,
                    'unidad': producto.unidad,
                    'subtotal': producto.precio_unitario,
                    'error': ''
                }
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
        if request.POST['action'] == 'guardar':
            try:
                data = {
                    "cliente_id" : 2,
                    "subtotal" : float(request.POST['detalles[subtotal]']),
                    "iva" : float(request.POST['detalles[iva]']), 
                    "total" : float(request.POST['detalles[total]']) 
                }
                orden = Orden()
                orden.cliente_id = int(request.POST['cliente[id]'])
                orden.subtotal = float(request.POST['detalles[subtotal]'])
                orden.iva = float(request.POST['detalles[iva]'])
                orden.total = float(request.POST['detalles[total]'])
                orden.tipo = request.POST['tipo']
                orden.lugar = request.POST['lugar']
                orden.estado = request.POST['estado']
                orden.horometro = int(request.POST['horometro'])
                orden.recomendacion = request.POST['recomendaciones']
                orden.observacion = request.POST['observaciones']
                orden.tecnico = request.POST['tecnico']
                orden.recibe = request.POST['recibe']
                orden.equipo_id = int(request.POST['equipo[id]'])
                orden.save()
                servicios = json.loads(request.POST['servicios'])
                for x in servicios:
                    det_servicio = DetalleServicio()
                    serv = json.loads(json.dumps(servicios[x]))
                    det_servicio.orden_id = orden.id
                    det_servicio.servicio_id = int(serv['servicio'])
                    self._extracted_from_post_(serv, det_servicio)
                productos = json.loads(request.POST['productos'])
                for x in productos:
                    det_producto = detalleProducto()
                    prod = json.loads(json.dumps(productos[x]))
                    det_producto.producto_id = int(prod['producto'])
                    det_producto.orden_id = orden.id
                    self._extracted_from_post_(prod, det_producto)
                causas = json.loads(request.POST['causas'])
                for x in causas:
                    det_causas = DetalleCausas()
                    causa = json.loads(json.dumps(causas[x]))
                    det_causas.causa_id = int(causa['causa'])
                    det_causas.orden_id = orden.id
                    det_causas.save()
                
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
        if request.POST['action'] == 'aprobar':
            try:
                orden = Orden.objects.get(id = int(request.POST['id']))
                productos = detalleProducto.objects.filter(orden_id = int(request.POST['id']))
                print(vars(productos))
                for producto in productos:
                    prod = Producto.objects.get(id = producto.producto_id)
                    prod.cantidad = prod.cantidad - producto.cantidad
                    prod.save()
                orden.aprobacion = True
                orden.save()
                data['error'] = ''
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
    # TODO Rename this here and in `post`
    def _extracted_from_post_(self, arg0, arg1):
        arg1.cantidad = int(arg0['cantidad'])
        arg1.subtotal = float(arg0['subtotal'])
        arg1.precio = float(arg0['precio'])
        arg1.save()

class ordenUpdate(UpdateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'Orden/actualizar.html'


    def get_productos(self):
        productos = detalleProducto.objects.filter(orden_id = self.get_object().id)
        for producto in productos:
            prod = Producto.objects.get(id = producto.producto_id)
            producto.cantidadMax = prod.cantidad
        return productos
    
    def get_causas(self):
        return DetalleCausas.objects.filter(orden_id = self.get_object().id)
    
    def get_equipo(self):
        return Equipo.objects.get(pk = self.get_object().equipo_id)

    def get_servicios(self):
        return DetalleServicio.objects.filter(orden_id = self.get_object().id)
    
    def get_cliente(self):
        return Cliente.objects.get(pk = self.get_object().cliente_id)
    
    def get_tecnico(self):
        return Empleado.object.get(pk = self.get_object().tecnico)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.get_object().id
        context['cliente'] = self.get_cliente()       
        context['tecnico'] = self.get_tecnico()       
        context['equipo'] = self.get_equipo()       
        context['causas'] = self.get_causas()
        context['productos'] = self.get_productos()
        context['servicios'] = self.get_servicios()
        context['causas2'] = Causas.objects.all()
        context['servicios2'] = Servicio.objects.all()
        context['productos2'] = Producto.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)    
    
    def post(self, request, *args, **kwargs):       
        data = {}
        if request.POST['action'] == 'search-servicio':
            try:
                servicio = Servicio.objects.get(id = str(request.POST['nombre']))
                data = {
                    'servicio': servicio.id,
                    'nombre': servicio.nombre,
                    'categoria': str(servicio.categoria),
                    'cantidad': 1,
                    'precio': servicio.precio,
                    'subtotal': servicio.precio,
                    'error': ''
                }
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        if request.POST['action'] == 'search-producto':
            try:
                producto = Producto.objects.get(id = str(request.POST['nombre']))
                data = {
                    'producto': producto.id,
                    'nombre': producto.nombre,
                    'cantidadMax': producto.cantidad,
                    'cantidad': 1,
                    'precio': producto.precio_unitario,
                    'unidad': producto.unidad,
                    'subtotal': producto.precio_unitario,
                    'error': ''
                }
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
        if request.POST['action'] == 'search-causa':
            try:
                causa = Causas.objects.get(id = str(request.POST['nombre']))
                data = {
                    'causa': causa.id,
                    'nombre': causa.nombre,
                    'error': ''
                }
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
        if request.POST['action'] == 'guardar':
            try:
                data = {
                    "cliente_id" : 2,
                    "subtotal" : float(request.POST['detalles[subtotal]']),
                    "iva" : float(request.POST['detalles[iva]']), 
                    "total" : float(request.POST['detalles[total]']),
                    
                }
                data2={
                    "servicios2": self.get_servicios(),
                    "productos": self.get_productos()
                }
                orden = Orden.objects.get(id=request.POST['id'])
                orden.cliente_id = int(request.POST['cliente[id]'])
                orden.subtotal = float(request.POST['detalles[subtotal]'])
                orden.iva = float(request.POST['detalles[iva]'])
                orden.total = float(request.POST['detalles[total]'])
                orden.save()
                for servicio in data2['servicios2']:
                    detServicio = DetalleServicio.objects.get(id = servicio.id)
                    detServicio.delete()
                servicios = json.loads(request.POST['servicios'])
                print(servicios)
                for x in servicios:
                    det_servicio = DetalleServicio()
                    serv = json.loads(json.dumps(servicios[x]))
                    det_servicio.orden_id = orden.id
                    det_servicio.servicio_id = int(serv['servicio'])
                    self._extracted_from_post_(serv, det_servicio)
                for producto in data2['productos']:
                    detProducto = detalleProducto.objects.get(id = producto.id)
                    detProducto.delete()
                productos = json.loads(request.POST['productos'])
                for x in productos:
                    det_producto = detalleProducto()
                    prod = json.loads(json.dumps(productos[x]))
                    det_producto.producto_id = int(prod['producto'])
                    det_producto.orden_id = orden.id
                    self._extracted_from_post_(prod, det_producto)
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data)
        
    def _extracted_from_post_(self, arg0, arg1):
        arg1.cantidad = int(arg0['cantidad'])
        arg1.subtotal = float(arg0['subtotal'])
        arg1.precio = float(arg0['precio'])
        arg1.save()
    
class OrdenList(ListView):
    template_name = 'Orden/index.html'
    model = Orden
    context_object_name = 'ordenes'

    def get(self, request, *args, **kwargs):
        ordenes = Orden.objects.filter(id__contains = request.GET.get('search', ''))
        context = {
            'ordenes': ordenes
        }
        return render(request, self.template_name, context)
    
class EliminarOrden(DeleteView):
    model = Orden
    template_name = 'Control/orden_delete.html'
    success_url= '../../ordenes'


    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('ordenes')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

class OrdenPdfView(View):

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('ticket.html')
            orden = Orden.objects.get(pk=self.kwargs['pk'])
            cliente = Cliente.objects.get(pk = orden.cliente_id)
            equipo = Equipo.objects.get(pk = orden.equipo_id)
            causas = DetalleCausas.objects.filter(orden_id = self.kwargs['pk'])
            productos = detalleProducto.objects.filter(orden_id = self.kwargs['pk'])
            servicios = DetalleServicio.objects.filter(orden_id = self.kwargs['pk'])
            for cau in causas:
                causa = Causas.objects.get(id = cau.causa_id) 
                cau.nombre = causa.nombre
            for prod in productos:
                product = Producto.objects.get(id = prod.id) 
                prod.nombre = product.nombre
                prod.unidad = product.unidad
            for ser in servicios:
                servicio = Servicio.objects.get(id = ser.id)
                ser.nombre = servicio.nombre
                ser.categoria = servicio.categoria  
            context = {
                'title': 'primer pdf',
                'orden': Orden.objects.get(pk=self.kwargs['pk']),
                'cliente': cliente,
                'equipo': equipo,
                'causas': causas,
                'productos': productos,
                'servicios': servicios,
                'tecnico': Empleado.object.get(id = orden.tecnico)
            }
            html = template.render(context)
            pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
            return HttpResponse(pdf, content_type = 'application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('ordenes'))
