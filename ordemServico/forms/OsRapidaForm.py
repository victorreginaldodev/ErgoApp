from django.forms import ModelForm, Select, NumberInput, Textarea, DateInput
from ordemServico.models import MiniOS

class OsRapidaForm(ModelForm):
    
    class Meta:
        model = MiniOS
        fields = ['cliente', 'servico', 'quantidade', 'profile', 'descricao', 'data_recebimento']
        widgets = {
            'cliente': Select(attrs={
                'class': 'form-select form-control w-75', 
                'id': 'floatingSelect', 
                'aria-label': 'Selecione um cliente',
            }),
            'servico': Select(attrs={
                'class': 'form-select form-control w-75', 
                'id': 'floatingSelect', 
                'aria-label': 'Selecione um serviço',
            }),
            'quantidade': NumberInput(attrs={
                'class': 'form-control w-50',                
            }), 
            'profile': Select(attrs={
                'class': 'form-select form-control w-75', 
                'id': 'floatingSelect', 
                'aria-label': 'Selecione um perfil',
            }),
            'descricao': Textarea(attrs={
                'class': 'form-control textarea-control w-100',
                'style': 'height: 150px',
                'id': 'floatingTextarea2',
                'placeholder': 'Digite aqui as observações sobre esse serviço...',
                'rows': 8,
            }),
            'data_recebimento': DateInput(attrs={
                'type': 'date',
                'class': 'form-control w-75'
            }), 
        }
