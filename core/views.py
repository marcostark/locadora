from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def index(request):
    return render(request, 'core/index.html')

def funcionarios(request):
    return render(request, 'core/funcionarios.html')

def cargos(request):
    return render(request, 'core/cargos.html')

def veiculos(request):
    return render(request, 'core/veiculos.html')

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
    return render(request, 'core/locacoes.html')

def save_clientes(request):
    if(request.POST):
        clientes_data = request.POST.dict()
        nome = clientes_data.get('nome')
        cpf = clientes_data.get("cpf")
        status = clientes_data.get("status")
        pontos_fidelidades = clientes_data.get("pontosFidelidade")
        print(nome, cpf, status, pontos_fidelidades)
        return HttpResponse("This is a post request")
    else:
        return render(request, "core/clientes.html")