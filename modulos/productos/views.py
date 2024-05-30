from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Bienvenidos a la aplicación de Productos")


# API View
from rest_framework.response import Response
from rest_framework.views import APIView

from modulos.productos.models import Producto, TipoProducto

class ProductoView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        return Response({"productos": productos})
    

"""
# Actualización de la Vista de la API
from .serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Producto

class ProductoView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
"""

from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from modulos.productos.models import Producto
from modulos.productos.serializers import ProductoSerializer

# Create your views here.

class ProductoList(generics.ListCreateAPIView):
    """
    Lista de Productos
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los productos por pk
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



# Filtros y busqueda
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from modulos.productos.models import Producto
from modulos.productos.serializers import ProductoSerializer
from modulos.productos.filters import ProductoFilter

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductoFilter
    search_fields = ['nombre', 'marca', 'tipoproducto__nombre']

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer