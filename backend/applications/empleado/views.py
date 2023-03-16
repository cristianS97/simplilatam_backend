from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import Empleado
from .serializers import EmpleadoSerializer, CreaEmpleadoSerializer, OnlyEmpleadoSerializer

# Create your views here.
class EmpleadoListApiView(ListAPIView):
    serializer_class = OnlyEmpleadoSerializer
    
    def get_queryset(self):
        return Empleado.objects.all()
    
class EmpleadoCreateApiView(CreateAPIView):
    serializer_class = CreaEmpleadoSerializer

class EmpleadoDetailListApiView(RetrieveAPIView):
    serializer_class = EmpleadoSerializer
    
    def get_queryset(self):
        return Empleado.objects.all()

