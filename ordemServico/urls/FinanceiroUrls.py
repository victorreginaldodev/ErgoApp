from django.urls import path
from ordemServico.views.FinanceiroView import financeiro

urlpatterns = [
    path('financeiro/', financeiro, name='financeiro'),
]
