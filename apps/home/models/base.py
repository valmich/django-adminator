
from django.db import models
from django.contrib.auth.models import User
import uuid
import re


import datetime 
from django.core.exceptions import ValidationError

from apps.home.models.escolas import *
from apps.home.models.bairros import *
from apps.home.models.bancos import *


COR_RACA = [
    ('Branca', 'Branca'),
    ('Preta', 'Preta'),
    ('Amarela', 'Amarela'),
    ('Parda', 'Parda'),
    ('Indígena', 'Indígena'),
    ('Não respondeu', 'Não respondeu'),
]

SEXO = [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Não informado', 'Não informado'),
]

ID_GENERO = [
    ('É como seu Cérebro define seu gênero, homem ou mulher', (
        ('Binário', 'Binário'),
    )),

    ('É um termo para identidades de gênero que não são estritamente homem ou mulher', (
        ('Não Binário', 'Não Binário'),
    )),
]

ESTADO_CIVIL = [
    ('Casado', 'Casado'),
    ('Solteiro', 'Solteiro'),
    ('Viúvo', 'Viúvo'),
    ('Divorciado', 'Divorciado'),
    ('Desquitado ou separado judicialmente',
     'Desquitado ou separado judicialmente'),
    ('Não respondeu', 'Não respondeu'),
]

TIPO_TELEFONE = [
    ('FIX', "Fixo"),
    ('CEL', "Celular"),
    ('FAX', "Fax"),
    ('OUT', "Outro"),
]

TIPO_ENDERECO = [
    ('UNI', 'Único'),
    ('RES', 'Residencial'),
    ('COM', 'Comercial'),
    ('COB', 'Cobrança'),
    ('ENT', 'Entrega'),
    ('OUT', 'Outro'),
]

UF_SIGLA = [
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
]

COD_UF = [
    ('12', 'AC'),
    ('27', 'AL'),
    ('16', 'AP'),
    ('13', 'AM'),
    ('29', 'BA'),
    ('23', 'CE'),
    ('53', 'DF'),
    ('32', 'ES'),
    ('52', 'GO'),
    ('21', 'MA'),
    ('51', 'MT'),
    ('50', 'MS'),
    ('31', 'MG'),
    ('15', 'PA'),
    ('25', 'PB'),
    ('41', 'PR'),
    ('26', 'PE'),
    ('22', 'PI'),
    ('33', 'RJ'),
    ('24', 'RN'),
    ('43', 'RS'),
    ('11', 'RO'),
    ('14', 'RR'),
    ('42', 'SC'),
    ('35', 'SP'),
    ('28', 'SE'),
    ('17', 'TO'),
]
def validador_data_de_nascimento(value):
    if value >= datetime.date.today() or value <= datetime.date(1900, 1, 1):
        raise ValidationError("Informe uma data válida")
    return value



class Pessoa(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=32, null=True, blank=True)
    rg = models.CharField(max_length=32, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True, validators=[validador_data_de_nascimento])
    cor = models.CharField('Cor', max_length=15,
                           choices=COR_RACA, null=True, blank=True)

    sexo = models.CharField('Sexo', max_length=15,
                            choices=SEXO, null=True, blank=True)
    id_genero = models.CharField(
        'Identidade de Genero', max_length=15, choices=ID_GENERO, null=True, blank=True)
    escolaridade = models.CharField(
        'Escolaridade', max_length=34, choices=ESCOLARIDADE, null=True, blank=True)
    escola = models.CharField(max_length= 30, choices=ESCOLAS, null=True, blank=True)
    
    estado_civil = models.CharField(
        'Estado Civil', max_length=36, choices=ESTADO_CIVIL, null=True, blank=True)
    informacoes_adicionais = models.CharField(
        "Informações Adicionais", max_length=1055, null=True, blank=True)

    # Dados padrao
  
    endereco_padrao = models.ForeignKey(
        'home.Endereco', related_name="end_padrao", on_delete=models.CASCADE, null=True, blank=True)
    telefone_padrao = models.ForeignKey(
        'home.Telefone', related_name="tel_padrao", on_delete=models.CASCADE, null=True, blank=True)
    site_padrao = models.ForeignKey(
        'home.Site', related_name="sit_padrao", on_delete=models.CASCADE, null=True, blank=True)
    email_padrao = models.ForeignKey(
        'home.Email', related_name="ema_padrao", on_delete=models.CASCADE, null=True, blank=True)
    banco_padrao = models.ForeignKey(
        'home.Banco', related_name="ban_padrao", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def format_cpf(self):
        if self.cpf:
            return 'CPF: {}'.format(self.cpf)
        else:
            return ''

    @property
    def format_rg(self):
        if self.rg:
            return 'RG: {}'.format(self.rg)
        else:
            return ''

    def idade(self):
        if self.nascimento is None:
            self.nascimento = datetime.date.today()
        d = (datetime.date.today() -
             self.nascimento) // datetime.timedelta(days=365.2425)
        return str(d) + ' anos'

    # Sobre o objeto
    criado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Atualizar datas criacao edicao
        if not self.data_criacao:
            self.data_criacao = datetime.date.today()
        self.data_edicao = datetime.date.today()
        return super(Pessoa, self).save(*args, **kwargs)

    @property
    def cpf_apenas_digitos(self):
        if self.cpf:
            return re.sub('[./-]', '', self.cpf)

    @property
    def uf_padrao(self):
        if self.endereco_padrao:
            return self.endereco_padrao.uf
        else:
            return ''

    def __unicode__(self):
        s = u'%s' % (self.nome)
        return s

    def __str__(self):
        s = u'%s' % (self.nome)
        return s


class Endereco(models.Model):
    pessoa_end = models.ForeignKey(
        Pessoa, related_name="endereco", on_delete=models.CASCADE, null=True, blank=True)
    tipo_endereco = models.CharField(
        max_length=3, null=True, blank=True, choices=TIPO_ENDERECO)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True )

    bairro = models.CharField(
        max_length=64, choices=BAIRROS, null=True, blank=True)
    complemento = models.CharField(max_length=64, null=True, blank=True)
    pais = models.CharField(max_length=32, null=True,
                            blank=True, default='Brasil')
    cpais = models.CharField(max_length=5, null=True,
                             blank=True, default='1058')
    municipio = models.CharField(
        max_length=64, null=True, blank=True, default='Parauapebas')
    cmun = models.CharField('Código do Município',
                            max_length=9, null=True, blank=True)
    cep = models.CharField('CEP', max_length=16, null=True, blank=True)
    uf = models.CharField('UF', max_length=3, null=True,
                          blank=True, choices=UF_SIGLA)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    @property
    def format_endereco(self):
        return '{0}, {1} - {2}'.format(self.logradouro, self.numero, self.bairro)

    @property
    def format_endereco_completo(self):
        return '{0} - {1} - {2} - {3} - {4} - {5} - {6}'.format(self.logradouro, self.numero, self.bairro, self.municipio, self.cep, self.uf, self.pais)

    def __unicode__(self):
        s = u'%s, %s, %s (%s)' % (
            self.logradouro, self.numero, self.municipio, self.uf)
        return s

    def __str__(self):
        s = u'%s, %s, %s (%s)' % (
            self.logradouro, self.numero, self.municipio, self.uf)
        return s


class Telefone(models.Model):
    pessoa_tel = models.ForeignKey(
        Pessoa, related_name="telefone", on_delete=models.CASCADE)
    tipo_telefone = models.CharField(
        max_length=8, choices=TIPO_TELEFONE, null=True, blank=True)
    telefone = models.CharField(max_length=32)

    def __unicode__(self):
        return self.telefone.replac('(', '').replace(' ', '').replace(')', '').replace('-', '')

    def __str__(self):
        return self.telefone.replace('(', '').replace(' ', '').replace(')', '').replace('-', '')

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


class Email(models.Model):
    pessoa_email = models.ForeignKey(
        Pessoa, related_name="email", on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __unicode__(self):
        s = u'%s' % (self.email)
        return s

    def __str__(self):
        s = u'%s' % (self.email)
        return s


class Site(models.Model):
    pessoa_site = models.ForeignKey(
        Pessoa, related_name="site", on_delete=models.CASCADE)
    site = models.CharField(max_length=255)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __unicode__(self):
        s = u'%s' % (self.site)
        return s

    def __str__(self):
        s = u'%s' % (self.site)
        return s


class Banco(models.Model):
    pessoa_banco = models.ForeignKey(
        Pessoa, related_name="banco", on_delete=models.CASCADE)
    banco = models.CharField(
        max_length=3, choices=BANCOS, null=True, blank=True)
    agencia = models.CharField(max_length=8, null=True, blank=True)
    conta = models.CharField(max_length=32, null=True, blank=True)
    digito = models.CharField(max_length=8, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __unicode__(self):
        s = u'%s / %s / %s' % (self.get_banco_display(),
                               self.agencia, self.conta)
        return s

    def __str__(self):
        s = u'%s / %s / %s' % (self.get_banco_display(),
                               self.agencia, self.conta)
        return s


class Documento(models.Model):
    # Documentos
    def diretorio_upload(self, filename):
        return '{0}/{1}/{2}'.format('upload', self.cpf, filename)


    pessoa_documento = models.ForeignKey(
        Pessoa, related_name="documento", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=32)
    documento = models.ImageField(null=True, blank=True, upload_to="pessoa_documento/")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

# class Controle(models.Model):
#     pessoa_controle = models.OneToOneField(Pessoa, on_delete=models.PROTECT)
#     situacao = models.CharField('Situação Cadastral', max_length=15, choices=SITUACAO, blank=True, null=False)
#     dados_incompletos = models.BooleanField('Dados Incompletos', default=False)
#     documentacao_ilegivel = models.BooleanField('Documentação Ilegível', default=False)
#     obs_gerais = models.TextField('Observações Gerais', max_length=500, blank=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     class Meta:
#         ordering = ["nome"]

#     class Meta:
#         verbose_name = "Controle"
#         verbose_name_plural = "Controle"

#     def __str__(self):
#         return self.pessoa
