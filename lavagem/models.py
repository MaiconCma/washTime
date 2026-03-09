from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente
from carro.models import Carro


class Lavagem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lavagens')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='lavagens')
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name='lavagens')
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'Lavagem de {self.carro.placa} - {self.data}'