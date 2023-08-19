from django.shortcuts import render
from conciertos.models import Concierto

def conciertos(request):
    
    conciertos = Concierto.objects.all()
    
    
    return render(request, 'conciertos.html', {'conciertos': conciertos})