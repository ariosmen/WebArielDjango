from django.shortcuts import render

def fotos(request):
    return render(request, 'fotos.html')