from rest_framework import viewsets
from carro.models import Carro
from carro.serializer import CarroSerializer


class CarrosViewset(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
