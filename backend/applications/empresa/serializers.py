from rest_framework import serializers
from .models import Empresa
from applications.empleado.models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'rut', 'nombre', 'email')

class EmpresaSerializer(serializers.ModelSerializer):
    empleados = EmpleadoSerializer(many=True)
    class Meta:
        model = Empresa
        fields = ('id', 'rut', 'nombre', 'direccion', 'telefono', 'empleados')

class OnlyEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'rut', 'nombre')