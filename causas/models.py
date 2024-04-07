from django.db import models

class Causas(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Causa'
        verbose_name_plural = 'Causas'
        ordering = ['id']
