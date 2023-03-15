from django.db import models

# Create your models here.
class Empresa(models.Model):
    rut = models.CharField(verbose_name='Rut de la empresa', max_length=15, unique=True)
    nombre = models.CharField(verbose_name='Nombre de la empresa', max_length=30)
    direccion = models.CharField(verbose_name='Dirección de la empresa', max_length=50)
    telefono = models.CharField(verbose_name='Télefono de la empresa', max_length=15)

    def __str__(self):
        return self.nombre
