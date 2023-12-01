from django.shortcuts import render
from . models import Oferta
from rest_framework import viewsets
from .serializer import OfertaSerializer
# Create your views here.
# def usuariolist(request):
#     return render(request,'usuariolist.html')
class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    