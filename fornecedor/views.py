from rest_framework import viewsets

from fornecedor.models import Fornecedor
from fornecedor.serializer import FornecedorSerializer


class FornecedorViewset(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

