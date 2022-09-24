from rest_framework.viewsets import ModelViewSet
from core.models import Carro
from core.serializer import CarroSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer