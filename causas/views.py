from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class ListarCausas(ListView):
    model = Causas
    template_name = 'causas/index.html'
    context_object_name = 'causas'
    
    def get(self, request,  *args, **kwargs):
        causas = Causas.objects.filter(nombre__contains = request.GET.get('search', ''))
        form = CausasForm()
        context = {
            'causas': causas,
            'form':form
        }
        return render(request, 'causas/index.html', context)
    
    def post(self, request, *args, **kwargs):
        data = {"nombre" : str(request.POST['nombre'])}
        try:
            form = CausasForm(data)
            if form.is_valid:
                form.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
class EliminarCausas(DeleteView):
    model = Causas
    template_name = 'control/causas_confirm_delete.html'
    success_url = reverse_lazy('causas')

    def delete(self, request, *args, **kwargs):
        if is_ajax(request=self.request):
            return reverse_lazy('causas')
        self.object = self.get_object()
        self.object.delete()
        mensaje = f'La orden {self.model.id} eliminado correctamente'
        return JsonResponse({'mensaje': mensaje, 'error': 'No hay error'})

