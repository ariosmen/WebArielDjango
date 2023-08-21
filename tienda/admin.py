from django.contrib import admin
from tienda.models import Producto, CategoriaProd
from django.utils.html import format_html

admin.site.site_header = "Ariel Mendez"

class CategoriaProdAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    readonly_fields = ('create',)
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'create', 'precio', 'foto', )
    readonly_fields = ('create',)
    
    def foto(self, obj):
        return format_html("<img src={} width='130' />", obj.imagen.url)
    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(CategoriaProd, CategoriaProdAdmin)
