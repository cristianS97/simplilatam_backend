from django.urls import path
from .views import EmpleadoListApiView, EmpleadoCreateApiView, EmpleadoDetailListApiView

urlpatterns = [
    path('listadoEmpleado/', EmpleadoListApiView.as_view()),
    path('empleadoDetail/<int:pk>', EmpleadoDetailListApiView.as_view()),
    path('crearEmpleado/', EmpleadoCreateApiView.as_view())
]
