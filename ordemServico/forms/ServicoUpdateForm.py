from django.forms import ModelForm, Select
from django import forms
from ordemServico.models import Servico

class ServicoUpdateForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['status']
        widgets = {
            'status': Select(attrs={
                'class': 'form-select', 
                'class': 'form-control w-100',
            }),
        }
        

