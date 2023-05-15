from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('accounts/profile/', views.certificado, name='certificado'),
    path('precio', views.precio, name='precio'),
    path('exhibicion', views.exhibition, name='exhibicion'),
    path('service', views.service, name='service'),
    path('segunda', views.segunda, name='segunda'),
    path('login', login_view, name='login'),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
