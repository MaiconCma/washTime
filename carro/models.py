from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente  # Corrigindo a importação do Cliente

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=10, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relaciona com cliente
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com usuário
    
    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano}) - {self.placa}'
