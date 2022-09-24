from rest_framework.serializers import ModelSerializer

from core.models import Carro

class CarroSerializer(ModelSerializer):
    class Meta:
        model= Carro
        fields = "__all__"
