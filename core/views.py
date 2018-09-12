from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def funcionarios(request):
    return render(request, 'core/funcionarios.html')

def cargos(request):
    return render(request, 'core/cargos.html')

def veiculos(request):
    return render(request, 'core/veiculos.html')

def clientes(request):
    return render(request, 'core/clientes.html')

def locacoes(request):
    return render(request, 'core/locacoes.html')


