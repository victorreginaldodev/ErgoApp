# Generated by Django 4.0.6 on 2024-09-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordemServico', '0007_minios_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='minios',
            name='data_recebimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
