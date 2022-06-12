from rest_framework import serializers
from fornecedor.models import Fornecedor


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'cnpj', 'telefone', 'endereco', 'numero', 'bairro', 'cidade', 'estado', 'site']
