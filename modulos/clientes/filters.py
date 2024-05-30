# Apps/clientes/filters.py

import django_filters
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = {
            'nombreCliente': ['icontains'],
            'direccionCliente': ['icontains'],
            'telefonoCliente': ['icontains'],
            'correoCliente': ['icontains'],
        }