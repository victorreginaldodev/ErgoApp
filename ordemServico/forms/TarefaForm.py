from django.forms import ModelForm, Select, Textarea

from ordemServico.models import Tarefa, Servico

class TarefaForm(ModelForm):

    class Meta:
        model = Tarefa
        fields = ['servico', 'profile', 'descricao']
        widgets = {
            'servico': Select(attrs={
                'class': 'form-select', 
                'aria-label': 'Selecione um serviço'
            }),
            'profile': Select(attrs={
                'class': 'form-select', 
                'aria-label': 'Selecione um colaborador'
            }),
            'descricao': Textarea(attrs={
                'class': 'form-control textarea-control',
                'style': 'height: 150px',
                'placeholder': 'Descrição',
                'rows': 3,  
            }),
        }
