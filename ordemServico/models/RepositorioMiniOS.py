from django.db import models

class RepositorioMiniOS(models.Model):
    nome = models.CharField(
        max_length=50,
    )
    descricao = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )

    def __str__(self):
        return self.nome