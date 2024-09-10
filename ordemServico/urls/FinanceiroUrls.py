from django.urls import path
from ordemServico.views.FinanceiroView import financeiro, monitoramento_financeiro

urlpatterns = [
    path('financeiro/', financeiro, name='financeiro'),
    path('monitoramento_financeiro/', monitoramento_financeiro, name='monitoramento_financeiro'),
]
