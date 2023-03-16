# Generated by Django 4.1.7 on 2023-03-15 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("empresa", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Empleado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rut",
                    models.CharField(
                        max_length=15, unique=True, verbose_name="Rut del empleado"
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=30, verbose_name="Nombre del empleado"),
                ),
                (
                    "email",
                    models.CharField(
                        max_length=50, verbose_name="Dirección del empleado"
                    ),
                ),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="empresa.empresa",
                        verbose_name="Empresa",
                    ),
                ),
            ],
        ),
    ]