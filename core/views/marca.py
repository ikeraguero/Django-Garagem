from rest_framework.viewsets import ModelViewSet
from core.models import Marca
from core.serializer import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
