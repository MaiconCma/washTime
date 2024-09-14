from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produto, name='listar_produto'),  # Lista os produtos
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),  # Adicionar produto
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),  # Editar produto
    path('excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),  # Excluir produto
]
