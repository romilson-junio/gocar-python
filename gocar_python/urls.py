"""gocar_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from aluguel.views import AluguelViewset
from carro.views import CarrosViewset
from cliente.views import ClientesViewset
from fornecedor.views import FornecedorViewset
from rest_framework import routers

from gocar_python import settings

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewset)
router.register(r'carros', CarrosViewset)
router.register(r'alugueis', AluguelViewset)
router.register(r'fornecedores', FornecedorViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
