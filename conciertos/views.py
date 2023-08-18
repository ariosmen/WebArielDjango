from django.shortcuts import render

def conciertos(request):
    return render(request, 'conciertos.html')