from django.urls import path
from .views import EmpresaListApiView

urlpatterns = [
    path('listadoEmpresa/', EmpresaListApiView.as_view())
]
