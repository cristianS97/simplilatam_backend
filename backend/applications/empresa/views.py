from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Empresa
from .serializers import EmpresaSerializer

# Create your views here.
class EmpresaListApiView(ListAPIView):
    serializer_class = EmpresaSerializer
    
    def get_queryset(self):
        return Empresa.objects.all()

