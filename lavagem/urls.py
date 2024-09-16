# urls.py do app de lavagem
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_lavagem, name='listar_lavagem'),
    path('adicionar/<int:carro_id>/', views.adicionar_lavagem, name='adicionar_lavagem'),
    path('editar/<int:lavagem_id>/', views.editar_lavagem, name='editar_lavagem'),
    path('excluir/<int:lavagem_id>/', views.excluir_lavagem, name='excluir_lavagem'),
]
