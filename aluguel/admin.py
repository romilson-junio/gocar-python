from django.contrib import admin

# Register your models here.
from aluguel.models import Aluguel


class Alugueis(admin.ModelAdmin):
    list_display = ('id', 'idCliente', 'idCarro', 'idFornecedor', 'dataRetirada', 'dataDevolucao', 'horaRetirada', 'horaDevolucao', 'valor', 'status')
    list_display_links = ('id', 'idCliente', 'idCarro')
    search_fields = ('idCliente', 'idCarro',)


admin.site.register(Aluguel, Alugueis)
