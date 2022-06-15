from django.db import models


# Create your models here.
class Aluguel(models.Model):
    idFornecedor = models.IntegerField()

    dataRetirada = models.DateField()
    dataDevolucao = models.DateField()

    horaRetirada = models.TimeField()
    horaDevolucao = models.TimeField()

    idCliente = models.IntegerField()
    idCarro = models.IntegerField()

    status = models.CharField(max_length=10)

    valor = models.FloatField()

    def __str__(self):
        return self.status
