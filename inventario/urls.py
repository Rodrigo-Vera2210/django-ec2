
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',LoginView.as_view(template_name='login/login.html'), name='login'),
    path('', include('control.urls')),
    path('cliente/', include('clientes.urls')),
    path('causas/', include('causas.urls')),
    path('empleado/', include('empleados.urls')),
    path('logout/',logout_then_login, name='logout'),
]
