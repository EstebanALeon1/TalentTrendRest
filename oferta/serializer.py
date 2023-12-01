from rest_framework import serializers
from .models import Oferta

class OfertaSerializer(serializers.OfertaSerializer):
    class Meta:
        model = Oferta
        fields= "__all__"