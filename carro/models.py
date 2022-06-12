from django.db import models


# Create your models here.
class Carro(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='carros', blank=True, null=True)
    grupo = models.CharField(max_length=20)
    tamanhoMala = models.CharField(max_length=1)
    cor = models.CharField(max_length=30)

    abs = models.BooleanField()
    airbag = models.BooleanField()
    vidroEletrico = models.BooleanField()
    arcondicionado = models.BooleanField()
    travaEletrica = models.BooleanField()
    direcaoHidraulica = models.BooleanField()
    automatico = models.BooleanField()
    tetoSolar = models.BooleanField()

    portas = models.IntegerField()
    malas = models.IntegerField()
    assentos = models.IntegerField()

    motor = models.FloatField()
    valor = models.FloatField()

    def __str__(self):
        return self.nome
