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


# ATUALIZA

def atualiza_cliente(request, pk):
    data = {}
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente) #Passar o formulario preenchido

    # Verificar se o form é valido
    if form.is_valid():
        form.save()  # Salva
        return redirect('url_cliente')  # E redireciona para a listagem

    data['form'] = form
    data['clientes'] = cliente # Enviando a transação pela URL, para ser possivel remover

    return render(request, 'core/atualizacliente.html', data)


def atualiza_funcionario(request, pk):
    data = {}
    funcionario = Funcionario.objects.get(pk=pk)
    form = FuncionarioForm(request.POST or None, instance=funcionario) #Passar o formulario preenchido

    # Verificar se o form é valido
    if form.is_valid():
        form.save()  # Salva
        return redirect('url_funcionario')  # E redireciona para a listagem

    data['form'] = form

    return render(request, 'core/atualizafuncionario.html', data)


def atualiza_cargo(request, pk):
    data = {}
    cargo = Cargo.objects.get(pk=pk)
    form = CargoForm(request.POST or None, instance=cargo)

    if form.is_valid():
        form.save()
        return redirect('url_cargo')

    data['form'] = form

    return render(request, 'core/atualizacargo.html', data)


def atualiza_veiculo(request, pk):
    data = {}
    veiculo = Veiculo.objects.get(pk=pk)
    form = VeiculoForm(request.POST or None, instance=veiculo)

    # Verificar se o form é valido
    if form.is_valid():
        form.save()  # Salva
        return redirect('url_veiculo')  # E redireciona para a listagem

    data['form'] = form

    return render(request, 'core/atualizaveiculo.html', data)


def atualiza_locacao(request, pk):
    data = {}
    locacao = Locacao.objects.get(pk=pk)
    form = LocacaoForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        return redirect('url_locacao')

    data['form'] = form

    return render(request, 'core/atualizalocacao.html', data)

# REMOVER

def remover_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('url_cliente')

def remover_cargo(request, pk):
    cargo = Cargo.objects.get(pk=pk)
    cargo.delete()
    return redirect('url_cargo')

def remover_funcionario(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)
    funcionario.delete()
    return redirect('url_funcionario')

def remover_veiculo(request, pk):
    veiculo = Veiculo.objects.get(pk=pk)
    veiculo.delete()
    return redirect('url_veiculo')

def remover_locacao(request, pk):
    locacao = Locacao.objects.get(pk=pk)
    locacao.delete()
    return redirect('url_locacao')


