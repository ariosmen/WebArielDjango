from django.urls import path
from tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tienda/', views.tienda, name='tienda'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

