from django.contrib import admin
from .models import Cliente, Cargo, Funcionario

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Cargo)
admin.site.register(Funcionario)