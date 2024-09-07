from django.urls import path
from ordemServico.views.LiderTecnicoView import lider_tecnico

urlpatterns = [
    path('lider/', lider_tecnico, name='lider_tecnico'),
]
