from django.urls import path
from ordemServico.views.OrdemServicoView import criar_ordem_servico, home

urlpatterns = [
    path('criar/', criar_ordem_servico, name='criar_ordem_servico'),
    path('home/', home, name='home'),
]
