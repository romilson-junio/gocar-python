from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)

    endereco = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    telefone = models.CharField(max_length=17)
    estado = models.CharField(max_length=17)

    def __str__(self):
        return self.nome
