# Apps/productos/filters.py
import django_filters
from modulos.productos.models import Producto

class ProductoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    marca = django_filters.CharFilter(lookup_expr='icontains')
    precio_min = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_max = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')
    stockmin = django_filters.NumberFilter()
    cantidad_min = django_filters.NumberFilter(field_name='cantidad', lookup_expr='gte')
    cantidad_max = django_filters.NumberFilter(field_name='cantidad', lookup_expr='lte')

    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'precio_min', 'precio_max', 'stockmin', 'cantidad_min', 'cantidad_max', 'tipoproducto']