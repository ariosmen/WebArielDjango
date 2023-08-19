from django.db import models

class Concierto(models.Model):
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    fecha = models.DateField()
    lugar = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'conciertos'
        verbose_name = 'concierto'
        verbose_name_plural = 'conciertos'
        
