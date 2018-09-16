from django import forms
from .models import Cliente, Cargo, Funcionario

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pontos_fidelidade = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = ('nome','cpf','status','pontos_fidelidade')


class CargoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    salario = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cargo
        fields = ('nome','descricao','salario')

class FuncionarioForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_admissao = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'date','class': 'form-control'}))
    #cargo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Funcionario
        fields = ('nome','cpf','data_admissao','cargo')