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
from core.views import remover_cliente, remover_cargo, remover_funcionario, remover_veiculo, remover_locacao
from core.views import atualiza_cliente, atualiza_funcionario, atualiza_cargo
from core.views import  atualiza_veiculo, atualiza_locacao

urlpatterns = [
    path('admin/', admin.site.urls),

    path('funcionarios/', funcionarios, name='url_funcionario'),
    path('cargos/', cargos, name='url_cargo'),
    path('clientes/', clientes, name='url_cliente'),
    path('locacoes/', locacoes, name='url_locacao'),
    path('veiculos/', veiculos, name='url_veiculo'),

    path('atualizacliente/<int:pk>/', atualiza_cliente, name='url_atualizacliente'),
    path('atualizafuncionario/<int:pk>/', atualiza_funcionario, name='url_atualizafuncionario'),
    path('atualizacargo/<int:pk>/', atualiza_cargo, name='url_atualizacargo'),
    path('atualizaveiculo/<int:pk>/', atualiza_veiculo, name='url_atualizaveiculo'),
    path('atualizalocacao/<int:pk>/', atualiza_locacao, name='url_atualizalocacao'),

    path('remover_cliente/<int:pk>/', remover_cliente, name='url_removercliente'),
    path('remover_cargo/<int:pk>/', remover_cargo, name='url_removercargo'),
    path('remover_funcionario/<int:pk>/', remover_funcionario, name='url_removerfuncionario'),
    path('remover_veiculo/<int:pk>/', remover_veiculo, name='url_removerveiculo'),
    path('remover_locacao/<int:pk>/', remover_locacao, name='url_removerlocacao'),

    path('', index, name='url_index'),
]
