from django.urls import path
from ordemServico.views.PainelControleView import painel_de_controle

urlpatterns = [
    path('painel/', painel_de_controle, name='painel_de_controle')
]