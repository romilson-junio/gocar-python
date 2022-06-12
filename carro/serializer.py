from rest_framework import serializers
from carro.models import Carro


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id', 'nome', 'marca', 'descricao', 'grupo', 'tamanhoMala', 'abs', 'airbag', 'vidroEletrico', 'imagem', 'arcondicionado',
                  'travaEletrica', 'direcaoHidraulica', 'automatico', 'tetoSolar', 'portas', 'malas', 'assentos', 'motor', 'cor', 'valor']
