from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome