from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class EmpleadoManager(BaseUserManager):
    def _create_user(self,email,username,nombre,apellido,password, is_superuser,**extra_fields):
        if not email:
            raise ValueError('El empleado debe tener un correo electrónico')
        
        
        empleado = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombre = nombre, 
            apellido = apellido,
            is_superuser = is_superuser,
            **extra_fields,
        )
        empleado.set_password(password)
        empleado.save(using=self.db)
        return empleado
    
    def create_user(self,email,username,nombre,apellido,password=None, **extra_fields):
        print(self)
        print(**extra_fields)
        return self._create_user(email,username,nombre,apellido,password, False,**extra_fields)
    
    def create_superuser(self,email,username,nombre,apellido,password=None, **extra_fields):
        return self._create_user(email,username,nombre,apellido,password, True,**extra_fields)


class Empleado(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=20, null=False, blank=False)
    c_id = models.CharField('Cedula', max_length=10, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True)
    direccion = models.CharField(max_length=30, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    fecha_create = models.DateField(default=datetime.today())
    empleado_administrador = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    object = EmpleadoManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombre','apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']