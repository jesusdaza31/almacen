from rest_framework import serializers
from modulos.productos.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    # len_nombreProducto = serializers.SerializerMethodField()
    class Meta:
        model = Producto
        fields = "__all__"
        # exclude = ['passwordProducto']
        # fields = (
        #     'pk',
        #     'nombreProducto',
        #     'descripcionProducto',
        #     'precioProducto',
        # )

    # def get_len_nombreProducto(self, object):
    #     length = len(object.nombreProducto)
    #     return length

    # def validate(self, data):
    #     if data['nombreProducto'] == data['descripcionProducto']:
    #         raise serializers.ValidationError('Nombre y Descripción No pueden ser iguales')
    #     else:
    #         return data

    def validate_nombreProducto(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Nombre no puede ser tan corto')
        else:
            return value

    def validate_precioProducto(self, value):
        if value <= 0:
            raise serializers.ValidationError('El precio debe ser mayor que 0')
        else:
            return value


# Filtros y busqueda
from rest_framework import serializers
from modulos.productos.models import Producto, TipoProducto

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'