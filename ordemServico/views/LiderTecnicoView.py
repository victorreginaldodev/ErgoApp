from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ordemServico.models import Servico, Tarefa
from ordemServico.forms import ServicoUpdateForm, TarefaForm

# Definindo o inlineformset_factory com os campos explicitamente
FormTarefaInlineFormset = inlineformset_factory(
    Servico,
    Tarefa,
    form=TarefaForm,
    fields=['profile', 'descricao'],
    extra=1
)

@login_required
def lider_tecnico(request):
    # Filtra serviços com status 'em_espera'
    novos_servicos = Servico.objects.filter(status='em_espera')
    qtd_novos_servicos = novos_servicos.count()

    # Filtra serviços com tarefas em andamento e remove duplicatas
    servicos_em_andamento = Servico.objects.filter(tarefa__status='em_andamento').distinct()
    qtd_servicos_em_andamento = servicos_em_andamento.count()

    # Filtra serviços com tarefas concluídas e remove duplicatas
    servicos_finalizados = Servico.objects.filter(tarefa__status='concluida').distinct()
    qtd_servicos_finalizados = servicos_finalizados.count()


    # Formulário para atualizar o serviço
    if request.method == 'POST' and 'formUpdate' in request.POST:
        servico_id = request.POST.get('servico_id')
        servico = get_object_or_404(Servico, id=servico_id)
        formUpdate = ServicoUpdateForm(request.POST, instance=servico)

        if formUpdate.is_valid():
            formUpdate.save()
            messages.success(request, 'Serviço atualizado com sucesso.')
            return redirect('lider_tecnico')
        else:
            messages.error(request, 'Erro ao tentar atualizar o serviço.')
    else:
        formUpdate = ServicoUpdateForm()

    # Formulário para criar tarefas relacionadas ao serviço
    if request.method == 'POST' and 'formTarefa' in request.POST:
        servico_id = request.POST.get('servico_id')
        servico = get_object_or_404(Servico, id=servico_id)
        form_tarefa = FormTarefaInlineFormset(request.POST, instance=servico)

        if form_tarefa.is_valid():
            form_tarefa.save()
            messages.success(request, 'Tarefas adicionadas com sucesso.')
            return redirect('lider_tecnico')
        else:
            messages.error(request, 'Erro ao tentar adicionar tarefas ao serviço.')
    else:
        servico_id = request.GET.get('servico_id')
        servico = get_object_or_404(Servico, id=servico_id) if servico_id else None
        form_tarefa = FormTarefaInlineFormset(instance=servico)

    context = {
        'novos_servicos': novos_servicos,
        'qtd_novos_servicos': qtd_novos_servicos,
        
        'servicos_em_andamento': servicos_em_andamento,
        'qtd_servicos_em_andamento': qtd_servicos_em_andamento,

        'servicos_finalizados': servicos_finalizados,
        'qtd_servicos_finalizados': qtd_servicos_finalizados,

        'formUpdate': formUpdate,
        'form_tarefa': form_tarefa,
        
    }

    return render(request, 'ordemServico/lider_tecnico.html', context)