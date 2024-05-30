"""
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenidos a la aplicación de Ventas")
"""

from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from modulos.ventas.models import Venta
from modulos.ventas.serializers import VentaSerializer

# Create your views here.

class VentaList(generics.ListCreateAPIView):
    """
    Lista de Ventas
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de las ventas por pk
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


# Filtros y busqueda
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from modulos.ventas.models import Venta
from modulos.ventas.serializers import VentaSerializer
from modulos.ventas.filters import VentaFilter

class VentaList(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = VentaFilter
    search_fields = ['usuario__username', 'cliente__nombre']

class VentaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
