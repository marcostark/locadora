from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        #nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        #cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        fields = ('nome','cpf','status','pontos_fidelidade')