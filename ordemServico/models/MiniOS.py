from django.db import models
from .Cliente import Cliente
from .Profile import Profile
from .RepositorioMiniOS import RepositorioMiniOS

class MiniOS(models.Model):
    STATUS = (
        ('nao_iniciado', 'NÃO INICIADO'),
        ('em_andamento', 'EM ANDAMENTO'),
        ('finalizada', 'FINALIZADA'),
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    servico = models.ForeignKey(RepositorioMiniOS, on_delete=models.PROTECT)
    quantidade = models.IntegerField(null=True, blank=True, default=1)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    descricao = models.CharField(null=True, blank=True, max_length=255)
    data_recebimento = models.DateField(null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_termino = models.DateField(null=True, blank=True)
    status = models.CharField(null=True, blank=True, choices=STATUS, max_length=15, default='nao_iniciado')

    def __str__(self):
        return self.servico.nome
