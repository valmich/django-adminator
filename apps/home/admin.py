# -*- encoding: utf-8 -*-

import csv
from django.http import HttpResponse

from django.contrib import admin

from apps.home.models.base import ESTADO_CIVIL, ID_GENERO, Banco, Email, Endereco, Pessoa, Telefone
from apps.home.models.escolas import ESCOLARIDADE

from apps.home.models.resumo_incapacidade import Cid, LocalAvaliacao, Participacao, ResumoIncapacidade



admin.site.site_header = "DMI"
admin.site.site_title = "DMI Portal"
admin.site.index_title = "Bem vindo ao DMI"

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Exportar Seleção"

class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1

class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1

class BancoInline(admin.TabularInline):
    model = Banco
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['nome', 'idade', 'endereco_padrao', 'cpf_apenas_digitos']
    inlines = [EnderecoInline, TelefoneInline, EmailInline, BancoInline]   
    fields = ['nome', 'cpf','rg', 'nascimento','sexo', 'cor', 'id_genero', 'escolaridade', 'escola', 'estado_civil', 'informacoes_adicionais']
    
    actions = ["export_as_csv"]



class LocalAvaliacaoInline(admin.TabularInline):
    model = LocalAvaliacao
    extra = 1

class ParticipacaoInline(admin.TabularInline):
    model = Participacao
    extra = 1


@admin.register(ResumoIncapacidade)
class ResumoIncapacidadeAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_per_page = 250
    actions = ["export_as_csv"]

@admin.register(Cid)
class CidAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_per_page = 250
    actions = ["export_as_csv"]