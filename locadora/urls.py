"""locadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core.views import index, funcionarios, cargos, clientes, locacoes, veiculos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', funcionarios, name='url_funcionario'),
    path('cargos/', cargos, name='url_cargo'),
    path('clientes/', clientes, name='url_cliente'),
    path('locacoes/', locacoes, name='url_locacao'),
    path('veiculos/', veiculos, name='url_veiculo'),

    path('', index, name='url_index'),
]
