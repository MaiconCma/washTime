from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_carro, name='listar_carro'),  # Lista os carros
    path('adicionar/', views.adicionar_carro, name='adicionar_carro'),  # Adicionar carro
    path('editar/<int:carro_id>/', views.editar_carro, name='editar_carro'),  # Editar carro
    path('excluir/<int:carro_id>/', views.excluir_carro, name='excluir_carro'),  # Excluir carro
]
