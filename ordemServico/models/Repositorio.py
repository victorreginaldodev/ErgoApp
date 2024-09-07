from django.db import models

class Repositorio(models.Model):
    nome = models.CharField(
        max_length=100
    )
    descricao = models.CharField(
        null=True, 
        blank=True,
        max_length=255,
    )

    def __str__(self):
        return self.nome