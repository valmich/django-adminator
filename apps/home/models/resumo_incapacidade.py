# from typing_extensions import Self
from django.db import models

from decimal import Decimal

from django.utils import timezone
from datetime import datetime

### LISTA DE RESPOSTAS ###
# LATERALIDADE = [
#     ('Ambidestro', 'Ambidestro'),
#     ('Direita', 'Direita'),
#     ('Esquerda', 'Esquerda'),
# ]

# TRATAMENTO = [
#     ('Eventual', 'Eventual'),
#     ('Contínuo', 'Contínuo'),
# ]

# REDUZ_EFEITOS_ADVERSOS = [
#     ('Não produz efeitos adversos', 'Não produz efeitos adversos'),
#     ('Efeitos adversos pontuais', 'Efeitos adversos pontuais'),
#     ('Efeitos adversos regulares', 'Efeitos adversos regulares'),
#     ('Efeitos adversos diários', 'Efeitos adversos diários'),
# ]

# NECESSITA = [
#     ('Continuamente', 'Continuamente'),
#     ('Eventualmente', 'Eventualmente'),
#     ('Frequentemente', 'Frequentemente'),
#     ('Necessita, mas não tem acesso', 'Necessita, mas não tem acesso'),
# ]

# NECESSITA_OUTRO = [
#     ('Pontuais', 'Pontuais (menos de 15 dias por mês)'),
#     ('Regulares', 'Regulares (mais de 15 dias por mês)'),
#     ('Diarios', 'Diarios'),
#     ('Necessita, mas não tem acesso', 'Necessita, mas não tem acesso'),

# ]

# REALIZOU_CIRURGIA = [
#     ('Não', 'Não'),
#     ('Apenas uma', 'Apenas uma'),
#     ('De duas a cinco', 'De duas a cinco'),
#     ('Mais de cinco', 'Mais de cinco'),
# ]

# NECESSITA_CIRURGIA = [
#     ('Não', 'Não'),
#     ('Sim', 'Sim'),
#     ('Necessita, mas não tem acesso', 'Necessita, mas não tem acesso'),
# ]

# EVOLUCAO_GLOBAL = [
#     ('Estabilização', 'Estabilização'),
#     ('Redução de funcionalidade flutuante', 'Redução de funcionalidade flutuante'),
#     ('Agravamento', 'Agravamento'),
#     ('Prograssão significativa', 'Prograssão significativa'),
#     ('Melhora', 'Melhora'),
#     ('Indefinida', 'Indefinida'),
# ]

ORIGEM_AGRAVO = [
    ('Congênita', 'Congênita'),
    ('Complicação no parto', 'Complicação no parto'),
    ('Doença', 'Doença'),
    ('Dependência química', 'Dependência química'),
    ('Violência', 'Violência'),
    ('Acidente de Trabalho / Doença ocupacional ou relacionado ao trabalho*', 'Acidente de Trabalho / Doença ocupacional ou relacionado ao trabalho*'),
    ('Acidente de Trânsito', 'Acidente de Trânsito'),
    ('Acidente de outra natureza', 'Acidente de outra natureza'),
    ('Ignorada', 'Ignorada'),
    ('Outra causa, especifique', 'Outra causa, especifique'),

]

# REAVALIACAO = [
#     ('6 meses a menos de 1 ano', '6 meses a menos de 1 ano'),
#     ('1 ano a menos de 2 anos', '1 ano a menos de 2 anos'),
#     ('2 anos a menos de 5 anos', '2 anos a menos de 5 anos'),
#     ('5 anos ou mais', '5 anos ou mais'),
# ]

INCAPACIDADE = [
    ('Auditiva', 'Auditiva'),
    ('Intelectual/Cognitiva', 'Intelectual/Cognitiva'),
    ('Motora', 'Motora'),
    ('Visual', 'Visual'),
    ('Mental', 'Mental'),
]


class Cid(models.Model):
    cid = models.CharField(max_length=255)

    class Meta:
        verbose_name = "CID"

    def __unicode__(self):
        s = u'%s' % (self.cid)
        return s

    def __str__(self):
        s = u'%s' % (self.cid)
        return s

class LocalAvaliacao(models.Model):
    local_avaliacao = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Local de Avaliação"

    def __unicode__(self):
        s = u'%s' % (self.local_avaliacao)
        return s

    def __str__(self):
        s = u'%s' % (self.local_avaliacao)
        return s


class ResumoIncapacidade(models.Model):
    sem_diagnostico = models.BooleanField('Sem diagnóstico etiológico definido', null=True, blank=True)
    
    categoria = models.CharField(
        max_length=69, choices=ORIGEM_AGRAVO, default='Ignorada')
    cid = models.ForeignKey(
        Cid, null=True, blank=True, on_delete=models.PROTECT)

    inicio_do_impedimento_principal = models.DateTimeField('Qual é a data aproximada do início do impedimento principal?', null=True, blank=True)

    descricao = models.CharField(max_length=255)
    inf_adicionais = models.CharField(max_length=255, null=True, blank=True)

    origem_agravo = models.CharField(
        max_length=69, choices=ORIGEM_AGRAVO, default='Ignorada')

    class Meta:
        verbose_name = "Resumo de Incapacidade"

    @property
    def format_incapacidade(self):
        return '{0}, {1} - {2}'.format(self.categoria, self.cid, self.descricao)

  
    def __unicode__(self):
        s = u'%s, %s, %s' % (
            self.categoria, self.cid, self.descricao)
        return s

    def __str__(self):
        s = u'%s, %s, %s' % (
            self.categoria, self.cid, self.descricao)
        return s

INFORMANTE = [
    ('A própria pessoa', 'A própria pessoa'),
    ('Pessoa de convívio próximo', 'Pessoa de convívio próximo'),
    ('Ambos', 'Ambos'),
]


class Participacao(models.Model):
    informante = models.CharField('Quem prestou as informações?',max_length=26, choices=INFORMANTE, null=True, blank=True)
    local_avaliacao = models.ForeignKey(
        LocalAvaliacao, null=True, blank=True, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Participação"

    @property
    def format_participante(self):
        return '{0} - {1}'.format(self.informante, self.local_avaliacao)

  
    def __unicode__(self):
        s = u'%s, %s' % (
            self.informante, self.local_avaliacao)
        return s

    def __str__(self):
        s = u'%s, %s' % (
            self.informante, self.local_avaliacao)
        return s

# ### ACOMPANHAMENTO MULTIDISCIPLINAR ###
# class AcompanhamentoMultidisciplinar(models.Model):
#     frequenta_alguma_instituicao_de_reabilitacao = models.CharField('Frequenta alguma instituição de reabilitação?', 
#             null=True, blank=True)
#     necessita_acompanhamento_caps = models.CharField('Necessita de acompanhamento no Centro de Atenção Psicossocial - CAPS?',
#             choices=NECESSITA_OUTRO, null=True, blank=True)
#     necessita_acompanhamento_centro_dia = models.CharField('Necessita de acompanhamento no Centro-Dia?',
#             choices=NECESSITA_OUTRO, null=True, blank=True)
#     necessita_acompanhamento_residencia_inclusiva = models.CharField('Necessita de acompanhamento na Residencia Inclusiva?',
#             choices=NECESSITA_OUTRO, null=True, blank=True)


# class FatoresGravidade(models.Model):
#     realizou_alguma_intervencao_cirurgica = models.CharField('Realizou alguma intervenção cirúrgica?',
#             choices=REALIZOU_CIRURGIA )
#     necessita_ser_submetido_intervencao_cirurgica = models.CharField ('Necessita ser submetido a intervenção cirúgica?',
#             choices=NECESSITA_OUTRO, null=True, blank=True)
#     para_criancas_indicar_se_possivel_presenca_de_atraso_principais_aquisicoes = models.CharField('Para crianças de 0 a 10 anos, indicar se há possível presença de atraso nas principais aquisições',
#             choices=NECESSITA_OUTRO, null=True, blank=True)

#     agravo_apresenta_impactos_no_funcionamento_geral_do_organismo = models.CharField('O agravo apresenta impactos no funcionamento geral do organismo (impacto psicológico, astenia, fadiga, lentidão, dor, espasticidade, perda ou ganho de peso, edemas, distúrbios de trânsito intestinal, náusea, prurido, tosse ou escarro, anosognosia - negação e falta de conhecimento da própria condição, entre outros',
#             max_length=50, choices=NECESSITA_OUTRO, null=True, blank=True)
#     agravo_apresenta_crises = models.CharField ('O agravo apresenta crises (convulsão, artralgia, descompensação neuropsiquiátrica, cardíaca, respiratória, entre outras) que reduzem a funcionalidade?',
#             max_length=50, choices=NECESSITA_OUTRO, null=True, blank=True)
#     perspectiva_de_evolução_global = models.CharField('Perspectiva de evolução global:',
#             max_length=50, choices=EVOLUCAO_GLOBAL, null=True, blank=True)
#     origem_circunstâncias_do_agravo_que_motiva_solicitação = models.CharField('Origem e circunstâncias do(s) agravo(s) que motiva(m) a solicitação:',
#             max_length=50, choices=ORIGEM_AGRAVO, null=True, blank=True)
#     qual_a_perspectiva_de_evolução_do_impedimento_apresentados_pelo_avaliado = models.CharField('Qual a perspectiva de evolução do(s) impedimento(s) apresentados pelo avaliado(a), considerando o tempo pregresso já vivenciado sob tal condição, a possibilidade de acesso a tratamentos necessários e as barreiras enfrentadas, com vistas a permitir efetiva participação na sociedade, em igualdade de condições com as demais pessoas?',
#             max_length=50, choices=EVOLUCAO_GLOBAL, null=True, blank=True)
#     por_base_respostas_anteriores_qual_prazo_estimado_para_reavaliação_do_caso = models.CharField('Tendo por base as respostas anteriores, qual o prazo estimado para reavaliação do caso?',
#             max_length=50, choices=REAVALIACAO, null=True, blank=True)