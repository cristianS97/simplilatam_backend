from django.urls import path
from .views import EmpresaListApiView, EmpresaCreateApiView

urlpatterns = [
    path('listadoEmpresa/', EmpresaListApiView.as_view()),
    path('crearEmpresa/', EmpresaCreateApiView.as_view())
]
