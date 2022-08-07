from pyexpat import model
from rest_framework.serializers import ModelSerializer

from core.models import Marca, Categoria, Carro

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class CarroSerializer(ModelSerializer):
    class Meta:
        model= Carro
        fields = "__all__"