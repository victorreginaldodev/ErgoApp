from django.forms import ModelForm, TextInput, Textarea
from ordemServico.models import Repositorio

class RepositorioForm(ModelForm):

    class Meta:
        model = Repositorio
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Digite a razão social do cliente'
            }),
            'descricao': Textarea(attrs={
                'class': 'form-control textarea-control w-100',
                'style': 'height: 150px',
                'id': 'floatingTextarea2',
                'placeholder': 'Digite aqui algumas observações importantes sobre esse cliente',
                'rows': 8,
            }),
        }