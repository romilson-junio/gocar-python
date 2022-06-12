from django.contrib import admin
from .models import Cliente


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'email', 'endereco', 'referencia', 'bairro', 'numero', 'telefone', 'estado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Cliente, Clientes)
