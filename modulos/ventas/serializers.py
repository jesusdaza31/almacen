

from rest_framework import serializers
from modulos.ventas.models import Venta, VentaProducto


from dataclasses import field
from statistics import mode



class VentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaProducto
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    productos = VentaProductoSerializer(many=True, read_only=True, source='ventaproducto_set')

    class Meta:
        model = Venta
        fields = ['id', 'fecha', 'descuento', 'total', 'subtotal', 'usuario', 'cliente', 'productos', 'created', 'updated']
