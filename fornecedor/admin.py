from django.contrib import admin

# Register your models here.
from fornecedor.models import Fornecedor


class Fornecedores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'telefone', 'endereco', 'numero', 'bairro', 'cidade', 'estado', 'site')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Fornecedor, Fornecedores)
