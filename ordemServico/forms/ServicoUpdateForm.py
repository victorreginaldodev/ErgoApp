from django.forms import ModelForm, Select,DateInput
from django import forms
from ordemServico.models import Servico

class ServicoUpdateForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['status', 'data_conclusao']
        widgets = {
            'status': Select(attrs={
                'class': 'form-select', 
                'class': 'form-control w-100',
            }),
            'data_conclusao': DateInput(attrs={
                'type': 'date',
                'class': 'form-control w-100'
            }),
        }
        

