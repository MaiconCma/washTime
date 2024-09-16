from django.db import models

from cliente.models import Carro, Cliente

class Lavagem(models.Model):
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.nome