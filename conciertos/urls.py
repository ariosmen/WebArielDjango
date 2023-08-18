from django.urls import path
from conciertos import views

urlpatterns = [
    path('conciertos/', views.conciertos, name='conciertos'),
]
