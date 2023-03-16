from django.urls import path
from .views import EmpleadoListApiView, EmpleadoCreateApiView

urlpatterns = [
    path('listadoEmpleado/', EmpleadoListApiView.as_view()),
    path('crearEmpleado/', EmpleadoCreateApiView.as_view())
]
