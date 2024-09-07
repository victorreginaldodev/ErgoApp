from django.db import models
from .OrdemServico import OrdemServico

class Anexo(models.Model):

    TIPO_ANEXO = (
        ('tecnico', 'TÉCNICO'),
        ('administrativo', 'ADMINISTRATIVO'),
    )

    ordem_servico = models.ForeignKey(
        OrdemServico, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    nome_documento = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    anexo = models.FileField(
        null=True,
        blank=True
    )
    tipo_anexo = models.CharField(
        max_length=15,
        choices=TIPO_ANEXO
    )

    def __str__(self):
        return self.nome_documento