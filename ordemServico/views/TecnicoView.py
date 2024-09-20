from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ordemServico.models import Tarefa

from ordemServico.forms import TarefaUpdateForm

@login_required
def tecnico(request):
    profile = request.user.profile

    # Filtra as tarefas relacionadas ao perfil do usuário logado
    tarefas_nao_iniciadas = Tarefa.objects.filter(status='nao_iniciada', profile=profile)
    qtd_tarefas_nao_iniciadas = tarefas_nao_iniciadas.count()

    tarefas_em_andamento = Tarefa.objects.filter(status='em_andamento', profile=profile)
    qtd_tarefas_em_andamento = tarefas_em_andamento.count()

    tarefas_finalizadas= Tarefa.objects.filter(status='concluida', profile=profile)
    qtd_tarefas_finalizadas = tarefas_finalizadas.count()


    # Manipulação do formulário de atualização da tarefa
    if request.method == 'POST' and 'formUpdate' in request.POST:
        tarefa_id = request.POST.get('tarefa_id')
        tarefa = get_object_or_404(Tarefa, id=tarefa_id, profile=profile)
        formUpdate = TarefaUpdateForm(request.POST, instance=tarefa)

        if formUpdate.is_valid():
            formUpdate.save()
            messages.success(request, 'Tarefa atualizada com sucesso.')
            return redirect('tecnico')
        else:
            messages.error(request, 'Erro ao tentar atualizar a tarefa.')
    else:
        formUpdate = TarefaUpdateForm()


    # Contexto para o template
    context = {
        'tarefas_nao_iniciadas': tarefas_nao_iniciadas,
        'qtd_tarefas_nao_iniciadas': qtd_tarefas_nao_iniciadas,
        'tarefas_em_andamento': tarefas_em_andamento,
        'qtd_tarefas_em_andamento': qtd_tarefas_em_andamento,
        'tarefas_finalizadas': tarefas_finalizadas,
        'qtd_tarefas_finalizadas': qtd_tarefas_finalizadas,

        'formUpdate': formUpdate,
    }

    return render(request, 'ordemServico/tecnico.html', context)