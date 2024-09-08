from django.forms import ModelForm, TextInput, Select, Textarea, NumberInput
from ordemServico.models import Cliente

class Clienteform(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'tipo_inscricao': Select(attrs={'class': 'form-select'}),
            'numero_inscricao': TextInput(attrs={'class': 'form-control'}),
            'ramo_atividade': TextInput(attrs={'class': 'form-control'}),
            'ramo_atividade_detalhado': TextInput(attrs={'class': 'form-control'}),
            'grau_risco': Select(attrs={'class': 'form-select'}),
            'tipo_cliente': Select(attrs={'class': 'form-select'}),
            'cnae': TextInput(attrs={'class': 'form-control'}),
            'observacao': Textarea(attrs={
                'class': 'form-control textarea-control w-100',
                'style': 'height: 150px',
                'id': 'floatingTextarea2',
                'placeholder': 'Digite aqui algumas observações importantes sobre esse cliente',
                'rows': 8,
            }),
        }