from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Count, Q, F
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ordemServico.forms import OrdemServicoUpdateForm
from ordemServico.models import OrdemServico

@login_required
def financeiro(request):
    if request.method == 'POST':
        # Debug para verificar se os dados estão sendo submetidos corretamente
        print(request.POST)
        
        ordem_servico_id = request.POST.get('ordem_servico_id')
        
        if ordem_servico_id:
            ordem_servico = get_object_or_404(OrdemServico, id=ordem_servico_id)
            form = OrdemServicoUpdateForm(request.POST, instance=ordem_servico)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Ordem de Serviço atualizada com sucesso.')
                return redirect('financeiro')
            else:
                messages.error(request, 'Erro ao atualizar a Ordem de Serviço. Verifique os dados fornecidos.')
        else:
            messages.error(request, 'ID da Ordem de Serviço não fornecido.')
    else:
        ordem_servico_id = request.GET.get('ordem_servico_id')
        
        if ordem_servico_id:
            ordem_servico = get_object_or_404(OrdemServico, id=ordem_servico_id)
            form = OrdemServicoUpdateForm(instance=ordem_servico)
        else:
            form = OrdemServicoUpdateForm()

    # Filtra ordens de serviço para faturar, futuros faturamentos e faturados
    para_faturar = OrdemServico.objects.annotate(
        total_servicos=Count('servico'),
        total_concluidos=Count('servico', filter=Q(servico__status='concluida'))
    ).filter(
        total_servicos=F('total_concluidos'),  # Todos os serviços concluídos
        faturamento='nao'  # Filtro para apenas ordens de serviço com faturamento "não"
    )

    futuros_faturamentos = OrdemServico.objects.filter(concluida='nao', faturamento='nao')
    faturados = OrdemServico.objects.filter(concluida='sim', faturamento='sim')

    # Calcula valores e contagens
    valor_total_concluidas = para_faturar.aggregate(Sum('valor'))['valor__sum'] or 0
    valor_total_para_faturar = para_faturar.aggregate(Sum('valor'))['valor__sum'] or 0
    valor_total_futuros_faturamentos = futuros_faturamentos.aggregate(Sum('valor'))['valor__sum'] or 0
    valor_total_faturados = faturados.aggregate(Sum('valor'))['valor__sum'] or 0

    contagem_concluidas = para_faturar.count()
    contagem_para_faturar = futuros_faturamentos.count()
    contagem_futuros_faturamentos = futuros_faturamentos.count()
    contagem_faturados = faturados.count()

    context = {
        'para_faturar': para_faturar,
        'futuros_faturamentos': futuros_faturamentos,
        'faturados': faturados,
        'valor_total_concluidas': valor_total_concluidas,
        'valor_total_para_faturar': valor_total_para_faturar,
        'valor_total_futuros_faturamentos': valor_total_futuros_faturamentos,
        'valor_total_faturados': valor_total_faturados,
        'contagem_concluidas': contagem_concluidas,
        'contagem_para_faturar': contagem_para_faturar,
        'contagem_futuros_faturamentos': contagem_futuros_faturamentos,
        'contagem_faturados': contagem_faturados,
        'form': form,
    }

    return render(request, 'ordemServico/financeiro.html', context)
