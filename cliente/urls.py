from django.urls import path
from . import views

urlpatterns = [
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),
    path('', views.listar_clientes, name='listar_clientes'),
    path('adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('adicionar_usuario/', views.adicionar_usuario, name='adicionar_usuario'),
]
