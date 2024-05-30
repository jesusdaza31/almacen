import django_filters
from modulos.ventas.models import Venta

class VentaFilter(django_filters.FilterSet):
    fecha = django_filters.DateFilter()
    descuento_min = django_filters.NumberFilter(field_name='descuento', lookup_expr='gte')
    descuento_max = django_filters.NumberFilter(field_name='descuento', lookup_expr='lte')
    total_min = django_filters.NumberFilter(field_name='total', lookup_expr='gte')
    total_max = django_filters.NumberFilter(field_name='total', lookup_expr='lte')
    subtotal_min = django_filters.NumberFilter(field_name='subtotal', lookup_expr='gte')
    subtotal_max = django_filters.NumberFilter(field_name='subtotal', lookup_expr='lte')

    class Meta:
        model = Venta
        fields = ['fecha', 'descuento_min', 'descuento_max', 'total_min', 'total_max', 'subtotal_min', 'subtotal_max', 'usuario', 'cliente']