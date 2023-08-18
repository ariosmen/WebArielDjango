from django.urls import path
from videos import views

urlpatterns = [
    path('videos/', views.videos, name='videos'),
]
