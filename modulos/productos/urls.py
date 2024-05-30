"""
from django.urls import path
from .views import home

urlpatterns = [
    path('inicio/', home, name='home'),
]



# configuracion de la URL de la API
from django.urls import path
from Apps.productos.views import ProductoView

app_name = "productos"
urlpatterns = [
    path('', ProductoView.as_view()),
]
"""

from django.urls import path
from modulos.productos.views import ProductoList, ProductoDetail

app_name = "productos"
urlpatterns = [
    path('', ProductoList.as_view(), name='producto-list'),
    path('<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
]