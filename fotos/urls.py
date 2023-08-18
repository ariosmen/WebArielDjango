from django.urls import path
from fotos import views

urlpatterns = [
    path('fotos/', views.fotos, name='fotos'),
]
