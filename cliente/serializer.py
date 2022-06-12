from rest_framework import serializers
from cliente.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'rg', 'email', 'senha', 'endereco', 'referencia', 'bairro', 'numero', 'telefone', 'estado']
