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

    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    tipo_inscricao = models.CharField(
        max_length=10,
        choices=TIPO_INSCRICAO, 
        default='cnpj',
        null=False,
        blank=False,
    )
    numero_inscricao = models.CharField(
        max_length=30, 
        unique=True,
        null=False,
        blank=False
    )
    tipo_cliente = models.CharField(
        choices=TIPO_CLIENTE, 
        default='gestao', 
        max_length=10,
        null=False,
        blank=False
    )
    observacao = models.CharField(
        null=True,
        blank=True, 
        max_length=255,
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    nome_representante = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    setor_representante = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    email_representante = models.EmailField(
        null=True,
        blank=True,
    )
    contato_representante = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )


    def __str__(self):
        return self.nome