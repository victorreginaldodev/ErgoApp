from django.db import models

class Cliente(models.Model):
    
    TIPO_CLIENTE = (
        ('gestao', 'Gestão'),
        ('avulso', 'Avulso'),
        ('fornecedor', 'Fornecedor')
    )

    TIPO_INSCRICAO = (
        ('cnpj', 'CNPJ'),
        ('cei', 'CEI'),
        ('cno', 'CNO'),
        ('caepf', 'CAEPF')
    )

    GRAU_RISCO = (
        (1, 'Grau 1'),
        (2, 'Grau 2'),
        (3, 'Grau 3'),
        (4, 'Grau 4')
    )

    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    tipo_inscricao = models.CharField(
        max_length=10,
        choices=TIPO_INSCRICAO, 
        default='cnpj'
    )
    numero_inscricao = models.CharField(
        max_length=30, 
        unique=True,
        null=False,
        blank=False
    )
    ramo_atividade = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    ramo_atividade_detalhado = models.CharField(
        max_length=255,
        blank=True, 
        null=True
    )
    grau_risco = models.IntegerField(
        choices=GRAU_RISCO
    )
    tipo_cliente = models.CharField(
        choices=TIPO_CLIENTE, 
        default='gestao', 
        max_length=10
    )
    cnae = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    observacao = models.CharField(
        blank=True, 
        null=True,
        max_length=255,
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome