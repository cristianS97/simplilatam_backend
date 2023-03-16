from django.urls import path
from .views import EmpresaListApiView, EmpresaCreateApiView, EmpresaDetailListApiView

urlpatterns = [
    path('listadoEmpresa/', EmpresaListApiView.as_view()),
    path('empresaDetail/<int:pk>', EmpresaDetailListApiView.as_view()),
    path('crearEmpresa/', EmpresaCreateApiView.as_view())
]
