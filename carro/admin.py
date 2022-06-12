from django.contrib import admin


# Register your models here.
from carro.models import Carro


class Carros(admin.ModelAdmin):
    list_display = (
    'id', 'nome', 'marca', 'descricao', 'grupo', 'tamanhoMala', 'abs', 'airbag', 'vidroEletrico', 'arcondicionado', 'imagem',
    'travaEletrica', 'direcaoHidraulica', 'automatico', 'tetoSolar', 'portas', 'malas', 'assentos', 'motor', 'cor', 'valor')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Carro, Carros)
