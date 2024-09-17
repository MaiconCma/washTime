from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produto, name='listar_produto'),
    path('produto/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produto/<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
    path('produto/<int:produto_id>/excluir/', views.excluir_produto, name='excluir_produto'),
    path('produto/<int:produto_id>/somar/', views.somar_produto, name='somar_produto'), 
    path('gastar/', views.registrar_gasto_produto, name='registrar_gasto_produto'),
]
