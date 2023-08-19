from django.contrib import admin
from conciertos.models import Concierto

class ConciertoAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'ciudad')

admin.site.register(Concierto, ConciertoAdmin)