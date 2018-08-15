from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:path>/', views.redirect, name='redirect'),
    path('--', views.api, name='api'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
