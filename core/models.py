from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    status = models.CharField(max_length=3)
    pontos_fidelidade = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome
