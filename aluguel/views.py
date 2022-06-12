from rest_framework import viewsets
from aluguel.models import Aluguel
from aluguel.serializer import AluguelSerializer


class AluguelViewset(viewsets.ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
