# Generated by Django 4.0.6 on 2024-09-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordemServico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='status',
            field=models.CharField(blank=True, choices=[('em_espera', 'EM ESPERA'), ('em_andamento', 'EM ANDAMENTO'), ('concluida', 'CONCLUÍDA')], default='em_espera', max_length=15, null=True),
        ),
    ]
