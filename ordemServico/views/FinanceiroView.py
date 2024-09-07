from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ordemServico.models import OrdemServico

from ordemServico.forms import OrdemServicoUpdateForm

@login_required
def financeiro(request):
    para_faturar = OrdemServico.objects.filter(concluida='sim', faturamento='nao')
    futuros_faturamentos = OrdemServico.objects.filter(concluida='nao', faturamento='nao')
    faturados = OrdemServico.objects.filter(concluida='sim', faturamento='sim')

    valor_total_para_faturar = para_faturar.aggregate(Sum('valor'))['valor__sum'] or 0
    valor_total_futuros_faturamentos = futuros_faturamentos.aggregate(Sum('valor'))['valor__sum'] or 0
    valor_total_faturados = faturados.aggregate(Sum('valor'))['valor__sum'] or 0

    contagem_para_faturar = para_faturar.count()        
    contagem_futuros_faturamentos = futuros_faturamentos.count()
    contagem_faturados = faturados.count()
        
    # TENTANDO EDITAR UMA ORDEM DE SERVIÇO
    if request.method == 'POST':
        ordem_servico_id = request.POST.get('ordem_servico_id')
        ordem_servico = get_object_or_404(OrdemServico, id=ordem_servico_id)
        form = OrdemServicoUpdateForm(request.POST, instance=ordem_servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ordem de Serviço atualizada com sucesso.')
            return redirect('financeiro')
        else:
            messages.error(request, 'Erro ao atualizar a Ordem de Serviço.')
    else:
        form = OrdemServicoUpdateForm()

    
    context = {
        'para_faturar': para_faturar,
        'futuros_faturamentos': futuros_faturamentos,
        'faturados': faturados,
        'valor_total_para_faturar': valor_total_para_faturar,
        'valor_total_futuros_faturamentos': valor_total_futuros_faturamentos,
        'valor_total_faturados': valor_total_faturados,
        'contagem_para_faturar': contagem_para_faturar,
        'contagem_futuros_faturamentos': contagem_futuros_faturamentos,
        'contagem_faturados': contagem_faturados,
        'form': form,
    }

    return render(request, 'ordemServico/financeiro.html', context)
