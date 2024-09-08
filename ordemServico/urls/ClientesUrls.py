from django.urls import path
from ordemServico.views.ClientesView import clientes

urlpatterns = [
    path('clientes/', clientes, name='clientes'),
]
