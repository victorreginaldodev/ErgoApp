from django.apps import AppConfig


class OrdemservicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ordemServico'

    def ready(self):
        import ordemServico.signals 