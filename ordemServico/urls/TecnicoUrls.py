from django.urls import path
from ordemServico.views.TecnicoView import tecnico

urlpatterns = [
    path('tecnico/', tecnico, name='tecnico'),
]