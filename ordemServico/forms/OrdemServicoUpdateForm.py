from django.forms import ModelForm, Select, TextInput, Textarea, NumberInput, CheckboxInput, DateInput
from django import forms
from ordemServico.models import OrdemServico

class OrdemServicoUpdateForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['faturamento', 'numero_nf', 'data_faturamento']
        widgets = {
            'faturamento': Select(attrs={
                'class': 'form-select', 
                'class': 'form-control w-100',
            }),

            'numero_nf': TextInput(attrs={
                'class': 'form-control w-100',
            }),

            'data_faturamento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control', 
                'class': 'form-control w-100'
            }),
        }
        