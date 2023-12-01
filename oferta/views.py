from django.shortcuts import render
from rest_framework import viewsets
from .models import Oferta
from .serializer import OfertaSerializer


class OfertaSerializer(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    