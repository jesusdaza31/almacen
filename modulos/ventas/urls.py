"""
from django.urls import path
from .views import home

urlpatterns = [
    path('inicio/', home, name='home'),
]

"""

from django.urls import path
from modulos.ventas.views import VentaList, VentaDetail

app_name = "ventas"
urlpatterns = [
    path('', VentaList.as_view(), name='venta-list'),
    path('<int:pk>/', VentaDetail.as_view(), name='venta-detail'),
]