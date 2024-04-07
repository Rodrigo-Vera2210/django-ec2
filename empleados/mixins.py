from django.shortcuts import redirect
from django.urls import reverse_lazy

class SuperUsuarioMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('orden_create')
    
class ValidarPermisosRequeridosMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perm(self):
        if isinstance(self.permission_required,str): 
            return(self.permission_required) 
        else: 
            return self.permission_required
        
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super(self).dispatch(request, *args, **kwargs)
        return redirect(self.get_url_redirect())
        