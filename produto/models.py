from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionando com o usuário que adicionou o produto

    def __str__(self):
        return self.nome
