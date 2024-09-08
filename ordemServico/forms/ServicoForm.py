from django import forms
from ordemServico.models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['repositorio', 'descricao'] 
        widgets = {
            'repositorio': forms.Select(attrs={
                'class': 'form-select', 
                'id': 'floatingSelect',
                'aria-label': 'Selecione um repositório',
                'class': 'form-control w-75',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control textarea-control w-100',
                'style': 'height: 150px',
                'id': 'floatingTextarea2',
                'placeholder': 'Digite aqui a descrição...',
                'rows': 8,
            }),
        }
