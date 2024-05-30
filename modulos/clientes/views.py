from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse


"""
def home(request):
    return HttpResponse("Bienvenidos a la aplicación de Clientes")



from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from Apps.clientes.models import Cliente
from Apps.clientes.serializers import ClienteSerializer

# Create your views here.


class ClienteList(generics.ListCreateAPIView):
 
    # Lista de Clientes


    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer



class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    
    #Retrieve, update or delete de los clientes por pk
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    








from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from rest_framework import status

from Apps.clientes.models import Cliente
from Apps.clientes.serializers import ClienteSerializer

# Create your views here.


class ClienteList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    #Lista de Clientes


    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





class ClienteDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    # Retrieve, update or delete de los clientes por pk

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
   
    
    
    
    # API usando vistas basadas en clases
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from Apps.clientes.models import Cliente
from Apps.clientes.serializers import ClienteSerializer, ClienteSerializer

# Create your views here.


class ClienteList(APIView):
 
    #Lista de Clientes


    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        # data = {"results": list(clientes.values("nombreCliente", "direccionCliente", "telefonoCliente", "correoCliente", "passwordCliente"))}
        # print(data)
        # return JsonResponse(data)
        serializer = ClienteSerializer(clientes, many=True)
        return Response({"clientes":serializer.data})

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(APIView):
    
    #Retrieve, update or delete de los clientes por pk
    
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response({"cliente":serializer.data})

    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      """
        
        
        
        
        

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from modulos.clientes.models import Cliente
from modulos.clientes.serializers import ClienteSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def cliente_list(request):
    
    #List all code snippets, or create a new snippet.
    
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cliente_detail(request, pk):
    
    #Retrieve, update or delete a code snippet.
    
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# Apps/clientes/views.py

from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from modulos.clientes.models import Cliente
from modulos.clientes.serializers import ClienteSerializer
from modulos.clientes.filters import ClienteFilter

class ClienteList(generics.ListCreateAPIView):
    """
    Lista de Clientes
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ClienteFilter
    search_fields = ['nombreCliente', 'direccionCliente', 'telefonoCliente', 'correoCliente']

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer