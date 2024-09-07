from django.forms import ModelForm, Select, TextInput, Textarea, NumberInput, CheckboxInput, DateInput
from django import forms
from ordemServico.models import OrdemServico

class OrdemServicoForm(ModelForm):
    
    class Meta:
        model = OrdemServico
        fields = '__all__'
        widgets = {
            'cliente': Select(attrs={
                'class': 'form-select', 
                'id': 'floatingSelect', 
                'aria-label': 'Selecione um cliente',
                'class': 'form-control w-75',
            }),
            'valor': TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'aria-label': 'Valor',
                'class': 'form-control w-100',
            }),
            'cobranca_imediata': Select(attrs={
                'class': 'form-select', 
                'id': 'floatingSelect', 
                'aria-label': 'Cobrar imediatamente?',
                'class': 'form-control w-100'
            }),
            'forma_pagamento': Select(attrs={
                'class': 'form-select', 
                'id': 'floatingSelect', 
                'aria-label': 'Forma de pagamento',
                'class': 'form-control w-100'
            }),
            'quantidade_parcelas': Select(attrs={
                'class': 'form-select', 
                'id': 'floatingSelect', 
                'aria-label': 'Quantidade de parcelas',
                'class': 'form-control w-100'
            }),
            'faturamento_1': DateInput(attrs={
                'class': 'form-control', 
                'id': 'faturamento_1', 
                'placeholder': 'Selecione a data', 
                'type': 'date',
                'class': 'form-control w-100'
            }),
            'nome_contato_envio_nf': TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput',
            }),
            'contato_envio_nf': TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput',
            }),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control textarea-control w-100',
                'style': 'height: 150px',
                'id': 'floatingTextarea2',
                'placeholder': 'Digite aqui as observações sobre o pagamento para a equipe financeira...',
                'rows': 8,
            }),
        }

