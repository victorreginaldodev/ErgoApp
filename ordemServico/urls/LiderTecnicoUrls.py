from django.urls import path
from ordemServico.views.LiderTecnicoView import lider_tecnico, tarefas

urlpatterns = [
    path('lider/', lider_tecnico, name='lider_tecnico'),
    path('tarefas/<int:servico_id>/', tarefas, name='tarefas' ),
]
