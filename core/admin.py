from django.contrib import admin
from .models import Cliente, Cargo, Funcionario, Veiculo

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Cargo)
admin.site.register(Funcionario)
admin.site.register(Veiculo)