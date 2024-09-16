from django.db import models
from django.contrib.auth.models import User

from carro.models import Carro

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionando com o usuário que adicionou o produto

    def __str__(self):
        return self.nome
class Gasto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que registrou o gasto
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome} gasto(s) no carro {self.carro.placa} ({self.carro.modelo})'
    
    