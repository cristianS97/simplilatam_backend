# simplilatam_backend
***
Desarrollo de la prueba técnica
Backend de la prueba

## Tabla de contenidos
1. [Descripción del proyecto](#informacion-general)
2. [Tecnologías usadas](#tecnologias)
3. [Aplicaciones](#aplicaciones)
4. [Docker](#docker)

## Información general
***
Backend del sitio el cual alimentara con información al frontend escrito en angular
En este se almacena la información de las empresas y empleados registrados

#### Información para crear una empresa
***
1. nombre: Nombre de la empresa a registrar
2. direccion: Dirección de la empresa
3. rut: Rut de la empresa
4. telefono: Télefono de la empresa

#### Información para crear un empleado
***
1. nombre: Nombre del empleado
2. email: Correo electronico del empleado
3. rut: Rut del empleado
4. empresa: Empresa a la que pertenece el empleado

## Tecnologías
***
Lista de tecnologías utilizadas en el proyecto:

1. [Python](https://www.python.org/): Versión 3.9.12
2. [Django](https://www.djangoproject.com/): Versión 4.1.7
3. [django-cors-headers](https://pypi.org/project/django-cors-headers/): Versión 3.14.0
4. [djangorestframework](https://www.django-rest-framework.org/): Versión 3.14.0

## Aplicaciones
1. empleado: Aplicación con las operaciones de lectura y creación de empleados de la API
2. empresa: Aplicación con las operaciones de lectura y creación de empresas de la API

## Docker
1. Crear imagen: docker build -t django-backend-simplilatam .
2. Correr imagen: docker run --name backend -p 8000:8000 -d django-backend-simplilatam