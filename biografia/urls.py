from django.urls import path
from biografia import views

urlpatterns = [
    path('biografia/', views.biografia, name='biografia'),
]
