from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente


class Carro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carros')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='carros')
    nome = models.CharField(max_length=100, blank=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'