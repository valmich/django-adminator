from django.contrib import admin

from apps.home.models.resumo_incapacidade import Cid, LocalAvaliacao, ResumoIncapacidade, Participacao

from apps.home.models.base import Pessoa, Email,Endereco, Telefone, Banco, Documento

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf','idade', 'id']


admin.site.register(Participacao)

admin.site.register(Cid)
admin.site.register(LocalAvaliacao)
admin.site.register(ResumoIncapacidade)
admin.site.register(Endereco)
admin.site.register(Email)
admin.site.register(Telefone)
admin.site.register(Banco)
admin.site.register(Documento)