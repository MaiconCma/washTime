from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', include('carro.urls')), 
    path('cliente/', include('cliente.urls')), 
    path('produto/', include('produto.urls')), 
]