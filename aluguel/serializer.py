from rest_framework import serializers
from aluguel.models import Aluguel


class AluguelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluguel
        fields = ['id', 'idCliente', 'idCarro', 'idFornecedor', 'dataRetirada', 'dataDevolucao', 'horaRetirada', 'horaDevolucao', 'valor', 'status']
