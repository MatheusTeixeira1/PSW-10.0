from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco = models.FloatField()

    def __str__(self):
        return self.nome_produto 