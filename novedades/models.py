from django.db import models

class Novedad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'novedadades'
        verbose_name = 'novedadad'
        verbose_name_plural = 'novedadades'
        ordering = ['-created']