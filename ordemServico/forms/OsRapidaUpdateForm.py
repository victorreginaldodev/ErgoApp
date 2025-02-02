from django.forms import ModelForm, Select, DateInput
from django import forms
from ordemServico.models import MiniOS, Cliente, RepositorioMiniOS, Profile

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

class OsRapidaFullUpdateForm(forms.ModelForm):

    class Meta:
        model = MiniOS
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-select w-100',
            }),
            'servico': forms.Select(attrs={
                'class': 'form-select w-100',
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control w-25',
                'min': '1',
            }),
            'profile': forms.Select(attrs={
                'class': 'form-select w-100',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'rows': '4',
                'placeholder': 'Digite a descrição do serviço',
            }),
            'data_recebimento': forms.DateInput(attrs={
                'class': 'form-control w-100',
                'type': 'date',
            }, format='%Y-%m-%d'),  # Ajusta o formato para o esperado pelo HTML5
            'data_inicio': forms.DateInput(attrs={
                'class': 'form-control w-100',
                'type': 'date',
            }, format='%Y-%m-%d'),
            'data_termino': forms.DateInput(attrs={
                'class': 'form-control w-100',
                'type': 'date',
            }, format='%Y-%m-%d'),
            'status': forms.Select(attrs={
                'class': 'form-select w-100',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(OsRapidaFullUpdateForm, self).__init__(*args, **kwargs)
        
        # Ordenar os clientes e serviços em ordem alfabética
        self.fields['cliente'].queryset = Cliente.objects.order_by('nome')
        self.fields['servico'].queryset = RepositorioMiniOS.objects.order_by('nome')
        self.fields['profile'].queryset = Profile.objects.order_by('user__username')
        
        # Ajustar os valores dos campos de data para o formato correto
        for field in ['data_recebimento', 'data_inicio', 'data_termino']:
            if self.instance and getattr(self.instance, field):
                self.fields[field].initial = getattr(self.instance, field).strftime('%Y-%m-%d')
