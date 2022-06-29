# Generated by Django 3.2.11 on 2022-06-28 16:34

import apps.home.models.base
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('banco', models.CharField(blank=True, choices=[('001', '001 - BANCO DO BRASIL S.A.'), ('003', '003 - BANCO DA AMAZONIA S.A.'), ('004', '004 - BANCO DO NORDESTE DO BRASIL S.A.'), ('012', '012 - BANCO STANDARD DE INVESTIMENTOS S.A.'), ('014', '014 - NATIXIS BRASIL S.A. BANCO MÚLTIPLO'), ('019', '019 - BANCO AZTECA DO BRASIL S.A.'), ('021', '021 - BANESTES S.A. BANCO DO ESTADO DO ESPIRITO SANTO'), ('024', '024 - BANCO DE PERNAMBUCO S.A. - BANDEPE'), ('025', '025 - BANCO ALFA S.A.'), ('029', '029 - BANCO BANERJ S.A.'), ('031', '031 - BANCO BEG S.A.'), ('033', '033 - BANCO SANTANDER (BRASIL) S.A.'), ('036', '036 - BANCO BRADESCO BBI S.A.'), ('037', '037 - BANCO DO ESTADO DO PARÁ S.A.'), ('040', '040 - BANCO CARGILL S.A.'), ('041', '041 - BANCO DO ESTADO DO RIO GRANDE DO SUL S.A.'), ('044', '044 - BANCO BVA S.A.'), ('045', '045 - BANCO OPPORTUNITY S.A.'), ('047', '047 - BANCO DO ESTADO DE SERGIPE S.A.'), ('062', '062 - HIPERCARD BANCO MÚLTIPLO S.A.'), ('063', '063 - BANCO IBI S.A. - BANCO MÚLTIPLO'), ('065', '065 - BANCO LEMON S.A.'), ('066', '066 - BANCO MORGAN STANLEY S.A.'), ('069', '069 - BPN BRASIL BANCO MÚLTIPLO S.A.'), ('070', '070 - BRB - BANCO DE BRASILIA S.A.'), ('072', '072 - BANCO RURAL MAIS S.A.'), ('073', '073 - BB BANCO POPULAR DO BRASIL S.A.'), ('074', '074 - BANCO J. SAFRA S.A.'), ('075', '075 - BANCO CR2 S/A'), ('076', '076 - BANCO KDB DO BRASIL S.A.'), ('077', '077 - BANCO INTERMEDIUM S/A'), ('078', '078 - BES INVESTIMENTO DO BRASIL S.A. - BANCO DE INVESTIMENTO'), ('079', '079 - JBS BANCO S/A'), ('081', '081 - CONCÓRDIA BANCO S.A.'), ('082', '082 - BANCO TOPÁZIO S.A.'), ('083', '083 - BANCO DA CHINA BRASIL S.A'), ('096', '096 - BANCO BM&F DE SERVIÇOS DE LIQUIDAÇÃO E CUSTÓDIA S.A.'), ('104', '104 - CAIXA ECONOMICA FEDERAL'), ('107', '107 - BANCO BBM S/A'), ('151', '151 - BANCO NOSSA CAIXA S.A.'), ('184', '184 - BANCO ITAÚ BBA S.A.'), ('204', '204 - BANCO BRADESCO CARTÕES S.A.'), ('208', '208 - BANCO UBS PACTUAL S.A.'), ('212', '212 - BANCO MATONE S.A.'), ('213', '213 - BANCO ARBI S.A.'), ('214', '214 - BANCO DIBENS S.A.'), ('215', '215 - BANCO COMERCIAL E DE INVESTIMENTO SUDAMERIS S.A.'), ('217', '217 - BANCO JOHN DEERE S.A.'), ('218', '218 - BANCO BONSUCESSO S.A.'), ('222', '222 - BANCO CALYON BRASIL S.A.'), ('224', '224 - BANCO FIBRA S.A.'), ('225', '225 - BANCO BRASCAN S.A.'), ('229', '229 - BANCO CRUZEIRO DO SUL S.A.'), ('230', '230 - UNICARD BANCO MÚLTIPLO S.A.'), ('233', '233 - BANCO GE CAPITAL S.A.'), ('237', '237 - BANCO BRADESCO S.A.'), ('241', '241 - BANCO CLASSICO S.A.'), ('243', '243 - BANCO MÁXIMA S.A.'), ('246', '246 - BANCO ABC BRASIL S.A.'), ('248', '248 - BANCO BOAVISTA INTERATLANTICO S.A.'), ('249', '249 - BANCO INVESTCRED UNIBANCO S.A.'), ('250', '250 - BANCO SCHAHIN S.A.'), ('254', '254 - PARANÁ BANCO S.A.'), ('260', '260 - NU PAGAMENTOS S.A.'), ('263', '263 - BANCO CACIQUE S.A.'), ('265', '265 - BANCO FATOR S.A.'), ('266', '266 - BANCO CEDULA S.A.'), ('300', '300 - BANCO DE LA NACION ARGENTINA'), ('318', '318 - BANCO BMG S.A.'), ('320', '320 - BANCO INDUSTRIAL E COMERCIAL S.A.'), ('341', '341 - BANCO ITAÚ S.A.'), ('366', '366 - BANCO SOCIETE GENERALE BRASIL S.A.'), ('370', '370 - BANCO WESTLB DO BRASIL S.A.'), ('376', '376 - BANCO J.P. MORGAN S.A.'), ('389', '389 - BANCO MERCANTIL DO BRASIL S.A.'), ('394', '394 - BANCO FINASA BMC S.A.'), ('399', '399 - HSBC BANK BRASIL S.A. - BANCO MULTIPLO'), ('409', '409 - UNIBANCO-UNIAO DE BANCOS BRASILEIROS S.A.'), ('412', '412 - BANCO CAPITAL S.A.'), ('422', '422 - BANCO SAFRA S.A.'), ('453', '453 - BANCO RURAL S.A.'), ('456', '456 - BANCO DE TOKYO-MITSUBISHI UFJ BRASIL S/A'), ('464', '464 - BANCO SUMITOMO MITSUI BRASILEIRO S.A.'), ('473', '473 - BANCO CAIXA GERAL - BRASIL S.A.'), ('477', '477 - CITIBANK N.A.'), ('479', '479 - BANCO ITAUBANK S.A.'), ('487', '487 - DEUTSCHE BANK S.A. - BANCO ALEMAO'), ('488', '488 - JPMORGAN CHASE BANK, NATIONAL ASSOCIATION'), ('492', '492 - ING BANK N.V.'), ('494', '494 - BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY'), ('495', '495 - BANCO DE LA PROVINCIA DE BUENOS AIRES'), ('505', '505 - BANCO CREDIT SUISSE (BRASIL) S.A.'), ('600', '600 - BANCO LUSO BRASILEIRO S.A.'), ('604', '604 - BANCO INDUSTRIAL DO BRASIL S.A.'), ('610', '610 - BANCO VR S.A.'), ('611', '611 - BANCO PAULISTA S.A.'), ('612', '612 - BANCO GUANABARA S.A.'), ('613', '613 - BANCO PECUNIA S.A.'), ('623', '623 - BANCO PANAMERICANO S.A.'), ('626', '626 - BANCO FICSA S.A.'), ('630', '630 - BANCO INTERCAP S.A.'), ('633', '633 - BANCO RENDIMENTO S.A.'), ('634', '634 - BANCO TRIANGULO S.A.'), ('637', '637 - BANCO SOFISA S.A.'), ('638', '638 - BANCO PROSPER S.A.'), ('641', '641 - BANCO ALVORADA S.A.'), ('643', '643 - BANCO PINE S.A.'), ('652', '652 - ITAÚ UNIBANCO BANCO MÚLTIPLO S.A.'), ('653', '653 - BANCO INDUSVAL S.A.'), ('654', '654 - BANCO A.J. RENNER S.A.'), ('655', '655 - BANCO VOTORANTIM S.A.'), ('707', '707 - BANCO DAYCOVAL S.A.'), ('719', '719 - BANIF - BANCO INTERNACIONAL DO FUNCHAL (BRASIL), S.A.'), ('721', '721 - BANCO CREDIBEL S.A.'), ('734', '734 - BANCO GERDAU S.A'), ('735', '735 - BANCO POTTENCIAL S.A.'), ('738', '738 - BANCO MORADA S.A'), ('739', '739 - BANCO BGN S.A.'), ('740', '740 - BANCO BARCLAYS S.A.'), ('741', '741 - BANCO RIBEIRAO PRETO S.A.'), ('743', '743 - BANCO SEMEAR S.A.'), ('745', '745 - BANCO CITIBANK S.A.'), ('746', '746 - BANCO MODAL S.A.'), ('747', '747 - BANCO RABOBANK INTERNATIONAL BRASIL S.A.'), ('748', '748 - BANCO COOPERATIVO SICREDI S.A.'), ('749', '749 - BANCO SIMPLES S.A.'), ('751', '751 - DRESDNER BANK BRASIL S.A. BANCO MULTIPLO'), ('752', '752 - BANCO BNP PARIBAS BRASIL S.A.'), ('753', '753 - NBC BANK BRASIL S. A. - BANCO MÚLTIPLO'), ('756', '756 - BANCO COOPERATIVO DO BRASIL S.A. - BANCOOB'), ('757', '757 - BANCO KEB DO BRASIL S.A.')], max_length=3, null=True)),
                ('agencia', models.CharField(blank=True, max_length=8, null=True)),
                ('conta', models.CharField(blank=True, max_length=32, null=True)),
                ('digito', models.CharField(blank=True, max_length=8, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'CID',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('tipo_endereco', models.CharField(blank=True, choices=[('UNI', 'Único'), ('RES', 'Residencial'), ('COM', 'Comercial'), ('COB', 'Cobrança'), ('ENT', 'Entrega'), ('OUT', 'Outro')], max_length=3, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(blank=True, choices=[('PERIMETRO URBANO', ()), ('ZONA CENTRAL', (('Cidade Nova', 'Cidade Nova'), ('Liberdade I', 'Liberdade I'), ('Liberdade II', 'Liberdade II'), ('Maranhão', 'Maranhão'), ('Guanabara', 'Guanabara'), ('da Paz', 'da Paz'), ('Paraíso', 'Paraíso'), ('Caetanópolis', 'Caetanópolis'), ('Esplanada', 'Esplanada'), ('Linha Verde', 'Linha Verde'), ('Primavera', 'Primavera'), ('União', 'União'), ('Rio Verde', 'Rio Verde'), ('Nova Vida', 'Nova Vida'))), ('ZONA NORDESTE', (('Minérios', 'Minérios'), ('Cidade Jardim', 'Cidade Jardim'))), ('ZONA NORTE', (('Alto Bonito', 'Alto Bonito'), ('Altamira', 'Altamira'), ('Betânia', 'Betânia'), ('Beira Rio', 'Beira Rio'), ('Vila Rica', 'Vila Rica'), ('Novo Horizonte', 'Novo Horizonte'), ('Jardim Canadá', 'Jardim Canadá'), ('Novo Viver', 'Novo Viver'), ('Polo Moveleiro', 'Polo Moveleiro'), ('Santa Luzia', 'Santa Luzia'), ('FAP', 'FAP'), ('Parque dos Carajás', 'Parque dos Carajás'), ('Habitar Feliz', 'Habitar Feliz'), ('Tropical', 'Tropical'), ('Vale do Sol', 'Vale do Sol'))), ('ZONA SUDESTE', (('Alvora', 'Alvora'), ('Amazônia', 'Amazônia'), ('Apoena', 'Apoena'), ('Novo Brasil', 'Novo Brasil'), ('Nova Carajás', 'Nova Carajás'))), ('ZONA SUL', (('Brasília', 'Brasília'), ('Jardim América', 'Jardim América'), ('Jardim Planalto', 'Jardim Planalto'), ('Morada Nova', 'Morada Nova'), ('Parque das Nações', 'Parque das Nações'), ('São Lucas', 'São Lucas'))), ('PERIMETRO RURAL', (('Área de Proteção Ambiental-APA', 'Área de Proteção Ambiental-APA'), ('Carlos Fonseca', 'Carlos Fonseca'), ('Cedere I', 'Cedere I'), ('Onalicio Barros', 'Onalicio Barros'), ('Paulo Fonteles', 'Paulo Fonteles'), ('Vila Sanção', 'Vila Sanção'), ('Outro', 'Outro')))], max_length=64, null=True)),
                ('complemento', models.CharField(blank=True, max_length=64, null=True)),
                ('pais', models.CharField(blank=True, default='Brasil', max_length=32, null=True)),
                ('cpais', models.CharField(blank=True, default='1058', max_length=5, null=True)),
                ('municipio', models.CharField(blank=True, default='Parauapebas', max_length=64, null=True)),
                ('cmun', models.CharField(blank=True, max_length=9, null=True, verbose_name='Código do Município')),
                ('cep', models.CharField(blank=True, max_length=16, null=True, verbose_name='CEP')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=3, null=True, verbose_name='UF')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocalAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_avaliacao', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Local de Avaliação',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('nome_secretaria', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(blank=True, max_length=32, null=True)),
                ('rg', models.CharField(blank=True, max_length=32, null=True)),
                ('nascimento', models.DateField(blank=True, null=True, validators=[apps.home.models.base.validador_data_de_nascimento])),
                ('cor', models.CharField(blank=True, choices=[('Branca', 'Branca'), ('Preta', 'Preta'), ('Amarela', 'Amarela'), ('Parda', 'Parda'), ('Indígena', 'Indígena'), ('Não respondeu', 'Não respondeu')], max_length=15, null=True, verbose_name='Cor')),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Não informado', 'Não informado')], max_length=15, null=True, verbose_name='Sexo')),
                ('id_genero', models.CharField(blank=True, choices=[('É como seu Cérebro define seu gênero, homem ou mulher', (('Binário', 'Binário'),)), ('É um termo para identidades de gênero que não são estritamente homem ou mulher', (('Não Binário', 'Não Binário'),))], max_length=15, null=True, verbose_name='Identidade de Genero')),
                ('escolaridade', models.CharField(blank=True, choices=[('Não se aplica', 'Não se aplica'), ('Nenhuma', 'Nenhuma'), ('Educação de Jovens e Adultos (EJA)', 'Educação de Jovens e Adultos (EJA)'), ('Educação infantil incompleta', 'Educação infantil incompleta'), ('Educação infantil completa', 'Educação infantil completa'), ('Fundamental incompleto', 'Fundamental incompleto'), ('Fundamental completo', 'Fundamental completo'), ('Médio incompleto', 'Médio incompleto'), ('Médio completo', 'Médio completo'), ('Superior incompleto', 'Superior incompleto'), ('Superior completo', 'Superior completo'), ('Especialização incompleto', 'Especialização incompleto'), ('Especialização completo', 'Especialização completo'), ('Mestrado incompleto', 'Mestrado incompleto'), ('Mestrado completo', 'Mestrado completo'), ('Doutorado incompleto', 'Doutorado incompleto'), ('Pós doutorado incompleto', 'Pós doutorado incompleto'), ('Pós doutorado completo', 'Pós doutorado completo')], max_length=34, null=True, verbose_name='Escolaridade')),
                ('estado_civil', models.CharField(blank=True, choices=[('Casado', 'Casado'), ('Solteiro', 'Solteiro'), ('Viúvo', 'Viúvo'), ('Divorciado', 'Divorciado'), ('Desquitado ou separado judicialmente', 'Desquitado ou separado judicialmente'), ('Não respondeu', 'Não respondeu')], max_length=36, null=True, verbose_name='Estado Civil')),
                ('informacoes_adicionais', models.CharField(blank=True, max_length=1055, null=True, verbose_name='Informações Adicionais')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_edicao', models.DateTimeField(auto_now_add=True)),
                ('banco_padrao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ban_padrao', to='home.banco')),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('email_padrao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ema_padrao', to='home.email')),
                ('endereco_padrao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_padrao', to='home.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Pcd',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.pessoa')),
                ('id_estrangeiro', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'PcD',
            },
            bases=('home.pessoa',),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('tipo_telefone', models.CharField(blank=True, choices=[('FIX', 'Fixo'), ('CEL', 'Celular'), ('FAX', 'Fax'), ('OUT', 'Outro')], max_length=8, null=True)),
                ('telefone', models.CharField(max_length=32)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('pessoa_tel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='home.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('pessoa_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site', to='home.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='ResumoIncapacidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_diagnostico', models.BooleanField(blank=True, null=True, verbose_name='Sem diagnóstico etiológico definido')),
                ('categoria', models.CharField(choices=[('Congênita', 'Congênita'), ('Complicação no parto', 'Complicação no parto'), ('Doença', 'Doença'), ('Dependência química', 'Dependência química'), ('Violência', 'Violência'), ('Acidente de Trabalho / Doença ocupacional ou relacionado ao trabalho*', 'Acidente de Trabalho / Doença ocupacional ou relacionado ao trabalho*'), ('Acidente de Trânsito', 'Acidente de Trânsito'), ('Acidente de outra natureza', 'Acidente de outra natureza'), ('Ignorada', 'Ignorada'), ('Outra causa, especifique', 'Outra causa, especifique')], default='Ignorada', max_length=69)),
                ('inicio_do_impedimento_principal', models.DateTimeField(blank=True, null=True, verbose_name='Qual é a data aproximada do início do impedimento principal?')),
                ('descricao', models.CharField(max_length=255)),
                ('inf_adicionais', models.CharField(blank=True, max_length=255, null=True)),
                ('origem_agravo', models.CharField(choices=[('Congênita', 'Congênita'), ('Complicação no parto', 'Complicação no parto'), ('Doença', 'Doença'), ('Dependência química', 'Dependência química'), ('Violência', 'Violência'), ('Acidente de Trabalho / Doença ocupacional ou relacionado ao trabalho*', 'Acidente de Trabalho / Doença ocupacional ou relacionado ao trabalho*'), ('Acidente de Trânsito', 'Acidente de Trânsito'), ('Acidente de outra natureza', 'Acidente de outra natureza'), ('Ignorada', 'Ignorada'), ('Outra causa, especifique', 'Outra causa, especifique')], default='Ignorada', max_length=69)),
                ('cid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.cid')),
            ],
            options={
                'verbose_name': 'Resumo de Incapacidade',
            },
        ),
        migrations.AddField(
            model_name='pessoa',
            name='site_padrao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sit_padrao', to='home.site'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='telefone_padrao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tel_padrao', to='home.telefone'),
        ),
        migrations.CreateModel(
            name='Participacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informante', models.CharField(blank=True, choices=[('A própria pessoa', 'A própria pessoa'), ('Pessoa de convívio próximo', 'Pessoa de convívio próximo'), ('Ambos', 'Ambos')], max_length=26, null=True, verbose_name='Quem prestou as informações?')),
                ('local_avaliacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.localavaliacao')),
            ],
            options={
                'verbose_name': 'Participação',
            },
        ),
        migrations.AddField(
            model_name='endereco',
            name='pessoa_end',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='home.pessoa'),
        ),
        migrations.AddField(
            model_name='email',
            name='pessoa_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='home.pessoa'),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('tipo', models.CharField(max_length=32)),
                ('documento', models.FileField(upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('pessoa_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documento', to='home.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='banco',
            name='pessoa_banco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banco', to='home.pessoa'),
        ),
    ]
