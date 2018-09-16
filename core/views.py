from django.shortcuts import render, redirect
from .forms import ClienteForm, CargoForm, FuncionarioForm
from .forms import VeiculoForm, LocacaoForm
from .models import Cliente, Cargo, Funcionario, Veiculo, Locacao

def index(request):
    return render(request, 'core/index.html')

def funcionarios(request):
    data = {}
    data['funcionarios'] = Funcionario.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('url_funcionario')
    else:
        data['form'] = FuncionarioForm()
    return render(request, 'core/funcionarios.html', data)

def cargos(request):
    data = {}
    data['cargos'] = Cargo.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('url_cargo')
    else:
        data['form'] = CargoForm()
    return render(request, 'core/cargos.html', data)

def veiculos(request):
    data = {}
    data['veiculos'] = Veiculo.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('url_veiculo')
    else:
        data['form'] = VeiculoForm()
    return render(request, 'core/veiculos.html', data)

def clientes(request):
    data = {}
    data['clientes'] = Cliente.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('url_cliente')
    else:
        data['form'] = ClienteForm()
        #form = ClienteForm()
    return render(request, 'core/clientes.html', data)

def locacoes(request):
    data = {}
    data['locacoes'] = Locacao.objects.all()  # Carregando clientes do banco

    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva
            return redirect('url_locacao')
    else:
        data['form'] = LocacaoForm()
        # form = ClienteForm()
    return render(request, 'core/locacoes.html', data)

# REMOÇÃO

def remover_clientes(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('url_cliente')

def remover_cargos(request, pk):
    cargo = Cargo.objects.get(pk=pk)
    cargo.delete()
    return redirect('url_cargo')

def remover_funcionarios(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)
    funcionario.delete()
    return redirect('url_funcionario')

def remover_veiculos(request, pk):
    veiculo = Veiculo.objects.get(pk=pk)
    veiculo.delete()
    return redirect('url_veiculo')


