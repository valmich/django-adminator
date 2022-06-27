from django.contrib import admin

from apps.home.models.resumo_incapacidade import Cid, AcompanhamentoAvaliacao, ResumoIncapacidade

from apps.home.models.base import Pessoa, Email,Endereco, Telefone, Banco, Documento

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf','idade', 'id']

admin.site.register(AcompanhamentoAvaliacao)

admin.site.register(Cid)

admin.site.register(ResumoIncapacidade)
admin.site.register(Endereco)
admin.site.register(Email)
admin.site.register(Telefone)
admin.site.register(Banco)
admin.site.register(Documento)