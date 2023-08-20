from django.contrib import admin
from novedades.models import Novedad

class NovedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    
admin.site.register(Novedad, NovedadAdmin)