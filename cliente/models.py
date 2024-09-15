from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientes')
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Carro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='carros')
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)

    def __str__(self):
        return self.placa
