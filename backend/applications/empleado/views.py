from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Empleado
from .serializers import EmpleadoSerializer

# Create your views here.
class EmpleadoListApiView(ListAPIView):
    serializer_class = EmpleadoSerializer
    
    def get_queryset(self):
        return Empleado.objects.all()
    
class EmpleadoCreateApiView(CreateAPIView):
    serializer_class = EmpleadoSerializer

