from django.forms import ModelForm, Select, Textarea
from django import forms

from ordemServico.models import MiniOS

class OsRapidaForm(ModelForm):

    class Meta:
        model = MiniOS
        fields = ['cliente', 'servico', 'profile', 'descricao']
        widgets = {
            'cliente': Select(attrs={
                'class': 'form-select', 
                'id': 'floatingSelect', 
                'aria-label': 'Selecione um cliente',
                'class': 'form-control w-75',
            }),
            'servico': Select(attrs={
                'class': 'form-select', 
                'id': 'floatingSelect', 
                'aria-label': 'Selecione um cliente',
                'class': 'form-control w-75',
            }),
            'profile': Select(attrs={
                'class': 'form-select', 
                'id': 'floatingSelect', 
                'aria-label': 'Selecione um cliente',
                'class': 'form-control w-75',
            }),
            'descricao': Textarea(attrs={
                'class': 'form-control textarea-control w-100',
                'style': 'height: 150px',
                'id': 'floatingTextarea2',
                'placeholder': 'Digite aqui as observações sobre esse serviço...',
                'rows': 8,
            }),
        }