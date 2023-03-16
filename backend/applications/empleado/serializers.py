from rest_framework import serializers
from .models import Empleado
from applications.empresa.models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'rut', 'nombre', 'direccion', 'telefono')

class EmpleadoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer()
    class Meta:
        model = Empleado
        fields = ('__all__')

class OnlyEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'rut', 'nombre')
