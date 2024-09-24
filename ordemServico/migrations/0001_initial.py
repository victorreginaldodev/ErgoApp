# Generated by Django 4.0.6 on 2024-09-24 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo_inscricao', models.CharField(blank=True, choices=[('cnpj', 'CNPJ'), ('cpf', 'CPF'), ('cei', 'CEI'), ('cno', 'CNO'), ('caepf', 'CAEPF')], default='cnpj', max_length=10, null=True)),
                ('numero_inscricao', models.CharField(blank=True, max_length=30, null=True)),
                ('tipo_cliente', models.CharField(blank=True, choices=[('gestao', 'Gestão'), ('avulso', 'Avulso'), ('fornecedor', 'Fornecedor')], default='gestao', max_length=10, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('nome_representante', models.CharField(blank=True, max_length=50, null=True)),
                ('setor_representante', models.CharField(blank=True, max_length=50, null=True)),
                ('email_representante', models.EmailField(blank=True, max_length=254, null=True)),
                ('contato_representante', models.CharField(blank=True, max_length=50, null=True)),
                ('cliente_ativo', models.CharField(blank=True, choices=[('sim', 'SIM'), ('nao', 'NÃO')], default='sim', max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_criador', models.CharField(blank=True, max_length=50, null=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('valor', models.FloatField(blank=True, default='0.0', null=True)),
                ('forma_pagamento', models.CharField(choices=[('pix', 'PIX'), ('credito', 'Crédito'), ('debto', 'Débto'), ('boleto', 'Boleto'), ('transferencia', 'Transferência'), ('dinheiro', 'Dinheiro'), ('check', 'Check'), ('outro', 'Outro')], default='boleto', max_length=30)),
                ('quantidade_parcelas', models.IntegerField(blank=True, choices=[(1, '1 parcela'), (2, '2 parcelas'), (3, '3 parcelas'), (4, '4 parcelas'), (5, '5 parcelas'), (6, '6 parcelas'), (7, '7 parcelas'), (8, '8 parcelas'), (9, '9 parcelas'), (10, '10 parcelas'), (11, '11 parcelas'), (12, '12 parcelas')], null=True)),
                ('cobranca_imediata', models.CharField(choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', max_length=5)),
                ('faturamento_1', models.DateField(blank=True, null=True)),
                ('nome_contato_envio_nf', models.CharField(default=' ', max_length=50)),
                ('contato_envio_nf', models.EmailField(default=' ', max_length=254)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('concluida', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', max_length=5, null=True)),
                ('faturamento', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao', max_length=5, null=True)),
                ('numero_nf', models.IntegerField(blank=True, null=True)),
                ('data_faturamento', models.DateField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ordemServico.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(1, 'Diretor'), (2, 'Administrativo'), (3, 'Líder Técnico'), (4, 'Sub-Líder Técnico'), (5, 'Técnico')], default=5)),
                ('cpf', models.CharField(max_length=14)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repositorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepositorioMiniOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('em_espera', 'EM ESPERA'), ('em_andamento', 'EM ANDAMENTO'), ('concluida', 'CONCLUÍDA')], default='em_espera', max_length=15, null=True)),
                ('data_conclusao', models.DateField(blank=True, null=True)),
                ('ordem_servico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ordemServico.ordemservico')),
                ('repositorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ordemServico.repositorio')),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True, max_length=255, null=True)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_termino', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('nao_iniciada', 'NÃO INICIADA'), ('em_andamento', 'EM ENDAMENTO'), ('concluida', 'CONCLUÍDA')], default='nao_iniciada', max_length=15, null=True)),
                ('ordem_servico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ordemServico.ordemservico')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordemServico.profile')),
                ('servico', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ordemServico.servico')),
            ],
        ),
        migrations.CreateModel(
            name='MiniOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, default=1, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_recebimento', models.DateField(blank=True, null=True)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_termino', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('nao_iniciado', 'NÃO INICIADO'), ('em_andamento', 'EM ANDAMENTO'), ('finalizada', 'FINALIZADA')], default='nao_iniciado', max_length=15, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ordemServico.cliente')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordemServico.profile')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ordemServico.repositoriominios')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('telefone', models.CharField(blank=True, max_length=30, null=True)),
                ('observacao', models.TextField(blank=True, max_length=255, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordemServico.cliente')),
            ],
        ),
    ]
