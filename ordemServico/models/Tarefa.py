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
        null=False,
        blank=False,
        default="",
         related_name='tarefas'
    ) 
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='tarefas_profile'
    )
    descricao = models.TextField(
        null=True, 
        blank=True,
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
        choices=STATUS,
        default='nao_iniciada'
    )

    def __str__(self):
        return f"Tarefa para {self.profile} em {self.servico}"