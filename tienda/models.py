from django.db import models

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=30)
    create = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'categoriasproductos'
        verbose_name = 'categoriaproducto'
        verbose_name_plural = 'categoriasproductos'
        
    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    create = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
