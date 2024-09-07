from django.db import models
from .Cliente import Cliente
from .Contato import Contato
from .Profile import Profile

class OrdemServico(models.Model):
    
    FORMA_PAGAMENTO = (
        ('pix', 'PIX'),
        ('credito', 'Crédito'),
        ('debto', 'Débto'),
        ('boleto', 'Boleto'),
        ('transferencia', 'Transferência'),
        ('dinheiro', 'Dinheiro'),
        ('check', 'Check'), 
        ('outro', 'Outro')      
    )

    COBRANCA_IMEDIATA = (
        ('sim', 'Sim'),
        ('nao', 'Não'),
    )

    QUANTIDADE_PARCELAS = (
        (1, '1 parcela'),
        (2, '2 parcelas'),
        (3, '3 parcelas'),
        (4, '4 parcelas'),
        (5, '5 parcelas'),
        (6, '6 parcelas'),
        (7, '7 parcelas'),
        (8, '8 parcelas'),
        (9, '9 parcelas'),
        (10, '10 parcelas'),
        (11, '11 parcelas'),
        (12, '12 parcelas'),
    )

    FATURAMENTO = (
        ('sim', 'Sim'),
        ('nao', 'Não'),
    )

    CONCLUIDA = (
        ('sim', 'Sim'),
        ('nao', 'Não'),
    )

    usuario_criador = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    data_criacao = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True
    )
    
    cliente = models.ForeignKey(
        Cliente, 
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

    valor = models.FloatField(
        null=True, 
        blank=True,
    )
    forma_pagamento = models.CharField(
        max_length=30, 
        choices=FORMA_PAGAMENTO,
        default='boleto',
        blank=True, 
        null=True,
    )
    quantidade_parcelas = models.IntegerField(
        blank=True, 
        null=True,
        choices=QUANTIDADE_PARCELAS,
    )
    cobranca_imediata = models.CharField(
        null=True, 
        blank=True,
        choices=COBRANCA_IMEDIATA,
        max_length=5,
        default=''
    )
    faturamento_1 = models.DateField(
        null=True,
        blank=True,
    )
    nome_contato_envio_nf = models.CharField(
        null=True,
        blank=True,
        max_length=50,
    )
    contato_envio_nf = models.EmailField(
        null=True,
        blank=True,
    )
    observacao = models.CharField(
        null=True, 
        blank=True,
        max_length=255,
    )

    concluida = models.CharField(
        default='nao',
        choices=CONCLUIDA,
        max_length=5,
        null=True,
        blank=True
    )

    faturamento = models.CharField(  
       null=True,
       blank=True,
       choices=FATURAMENTO,
       max_length=5
    )

    numero_nf = models.IntegerField(
        null=True, 
        blank=True
    )
    data_faturamento = models.DateField(
        null=True, 
        blank=True
    )

    def __str__(self):
        cliente_nome = self.cliente.nome if self.cliente else "Sem cliente"
        return f"{cliente_nome} - {self.valor}"
