from django.shortcuts import render

def novedades(request):
    return render(request, 'novedades.html')