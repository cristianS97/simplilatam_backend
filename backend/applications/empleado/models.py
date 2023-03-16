from django.db import models
from applications.empresa.models import Empresa

# Create your models here.
class Empleado(models.Model):
    rut = models.CharField(verbose_name='Rut del empleado', max_length=15, unique=True)
    nombre = models.CharField(verbose_name='Nombre del empleado', max_length=30)
    email = models.CharField(verbose_name='Dirección del empleado', max_length=50)
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

