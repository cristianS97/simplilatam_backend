from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import Empresa
from .serializers import EmpresaSerializer, OnlyEmpresaSerializer

# Create your views here.
class EmpresaListApiView(ListAPIView):
    serializer_class = OnlyEmpresaSerializer
    
    def get_queryset(self):
        return Empresa.objects.all()

class EmpresaCreateApiView(CreateAPIView):
    serializer_class = OnlyEmpresaSerializer

class EmpresaDetailListApiView(RetrieveAPIView):
    serializer_class = EmpresaSerializer
    
    def get_queryset(self):
        return Empresa.objects.all()


