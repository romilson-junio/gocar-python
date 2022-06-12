from django.db import models


# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)

    telefone = models.CharField(max_length=17)

    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=17)

    site = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
