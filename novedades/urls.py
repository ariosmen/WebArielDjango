from django.urls import path
from novedades import views

urlpatterns = [
    path('novedades/', views.novedades, name='novedades'),
]
