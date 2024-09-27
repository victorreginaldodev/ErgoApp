from django.urls import path
from ordemServico.views.ServicoView import servico

urlpatterns = [
    path('servico/', servico, name='servico'),
    path('servico/<int:id>/>', servico, name='servico'),
]