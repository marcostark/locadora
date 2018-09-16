from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    status = models.CharField(max_length=3)
    pontos_fidelidade = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    salario = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    data_admissao = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

