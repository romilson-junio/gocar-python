from rest_framework import serializers
from cliente.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:

        extra_kargs = {
            'senha': {'write_only':True},
            'email': {'write_only': True}
        }
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'rg', 'email', 'endereco', 'referencia', 'bairro', 'numero', 'telefone', 'estado']
