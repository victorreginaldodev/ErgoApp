from django.db import models
from .Servico import Servico
from .Profile import Profile
from .OrdemServico import OrdemServico

class Tarefa(models.Model):
    
    STATUS = (
        ('nao_iniciada', 'NÃO INICIADA'),
        ('em_andamento', 'EM ENDAMENTO'),
        ('concluida', 'CONCLUÍDA'),
    )

    ordem_servico = models.ForeignKey(
        OrdemServico,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    servico = models.ForeignKey(
        Servico, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    ) 
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    descricao = models.CharField(
        null=True, 
        blank=True,
        max_length=255
    )
    data_inicio = models.DateField(
        null=True,
        blank=True
    )
    data_termino = models.DateField(
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        choices=STATUS
    )

    def __str__(self):
        return f"Tarefa para {self.profile} em {self.servico}"