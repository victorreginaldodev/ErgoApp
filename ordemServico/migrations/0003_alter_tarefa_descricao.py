# Generated by Django 4.0.6 on 2024-09-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordemServico', '0002_alter_ordemservico_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
