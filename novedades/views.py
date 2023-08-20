from django.shortcuts import render
from novedades.models import Novedad

def novedades(request):
    
    novedades = Novedad.objects.all()
    
    return render(request, 'novedades.html', {'novedades': novedades})