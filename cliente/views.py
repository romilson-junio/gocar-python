from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from cliente.models import Cliente
from cliente.serializer import ClienteSerializer


class ClientesViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'senha']
