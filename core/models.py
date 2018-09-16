from django.db import models

# Create your models here.
STATUS= (
    ('A', 'Ativo'),
    ('I', 'Inativo'),
)

DEVOLUCAO_STATUS= (
    ('A', 'Em Aberto'),
    ('F', 'Fechada'),
)

class Cliente(models.Model):

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    #status = models.CharField(max_length=3)
    status = models.CharField(max_length=3, choices=STATUS)
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


class Veiculo(models.Model):

    modelo = models.CharField(max_length=200)
    cor = models.CharField(max_length=15)
    ano = models.IntegerField()
    placa = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.modelo


# <th>Código</th>
# <th>Data de Locação</th>
# <th>Data de Devolução</th>
# <th>Status</th>
# <th>Funcionário</th>
# <th>Cliente</th>
# <th>Veículo</th>

class Locacao(models.Model):

    data_locacao = models.DateField()
    data_devolucao = models.DateField()
    status = models.CharField(max_length=3, choices = DEVOLUCAO_STATUS)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Locações'

    def __str__(self):
        return self.status
