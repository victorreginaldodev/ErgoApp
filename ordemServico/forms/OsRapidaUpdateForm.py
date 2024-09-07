from django.forms import ModelForm, Select, TextInput, Textarea, NumberInput, CheckboxInput, DateInput
from django import forms
from ordemServico.models import MiniOS

class OsRapidaUpdateForm(forms.ModelForm):
    
    class Meta:
        model = MiniOS
        fields = ['status', 'data_inicio', 'data_termino']
        widgets = {
            'status': Select(attrs={
                'class': 'form-select', 
                'class': 'form-control w-100',
            }),
            'data_inicio': DateInput(attrs={
                'type': 'date',
                'class': 'form-control', 
                'class': 'form-control w-100'
            }),
            'data_termino': DateInput(attrs={
                'type': 'date',
                'class': 'form-control', 
                'class': 'form-control w-100'
            }),
        }