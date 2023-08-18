from django.shortcuts import render

def biografia(request):
    return render(request, 'biografia.html')