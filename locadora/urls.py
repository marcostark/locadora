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
from core.views import remover_clientes, remover_cargos, remover_funcionarios, remover_veiculos

urlpatterns = [
    path('admin/', admin.site.urls),

    path('funcionarios/', funcionarios, name='url_funcionario'),
    path('cargos/', cargos, name='url_cargo'),
    path('clientes/', clientes, name='url_cliente'),
    path('locacoes/', locacoes, name='url_locacao'),
    path('veiculos/', veiculos, name='url_veiculo'),

    path('remover_clientes/<int:pk>/', remover_clientes, name='url_removerclientes'),
    path('remover_cargos/<int:pk>/', remover_cargos, name='url_removercargos'),
    path('remover_funcionario/<int:pk>/', remover_funcionarios, name='url_removerfuncionario'),
    path('remover_veiculo/<int:pk>/', remover_veiculos, name='url_removerveiculo'),

    path('', index, name='url_index'),
]
