from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Empresa
from .serializers import EmpresaSerializer

# Create your views here.
class EmpresaListApiView(ListAPIView):
    serializer_class = EmpresaSerializer
    
    def get_queryset(self):
        return Empresa.objects.all()
    
class EmpresaCreateApiView(CreateAPIView):
    serializer_class = EmpresaSerializer

