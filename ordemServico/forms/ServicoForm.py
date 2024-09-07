from django.forms import ModelForm, Select, TextInput, Textarea, NumberInput, CheckboxInput, DateInput
from django import forms
from ordemServico.models import Servico

class ServicoForm(ModelForm):
    
    class Meta:
        model = Servico
        fields = ['repositorio', 'descricao']
        widgets = {
            'repositorio': Select(attrs={
                'class': 'form-select w-100',
                'aria-label': 'Selecione um serviço',
            }),
            'descricao': Textarea(attrs={
                'class': 'form-control w-100',
                'style': 'height: 150px',
                'placeholder': 'Faça a descrição do serviço',
                'rows': 3,
            }),
        }