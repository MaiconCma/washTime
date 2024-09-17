from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_carro, name='listar_carro'),  
    path('adicionar/', views.adicionar_carro, name='adicionar_carro'), 
    path('editar/<int:carro_id>/', views.editar_carro, name='editar_carro'), 
    path('excluir/<int:carro_id>/', views.excluir_carro, name='excluir_carro'), 
]
