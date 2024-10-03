from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Count, Q, F
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from ordemServico.forms import OrdemServicoUpdateForm
from ordemServico.models import OrdemServico, Profile

# Função que verifica se o usuário é 'Diretor', 'Administrativo' ou 'Líder Técnico'
def verificar_tipo_usuario(user):
    try:
        return user.profile.role in [1, 2, 3]
    except Profile.DoesNotExist:
        return False

@login_required
@user_passes_test(verificar_tipo_usuario)
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
        total_servicos=Count('servicos'),
        total_concluidos=Count('servicos', filter=Q(servicos__status='concluida'))
    ).filter(
        total_servicos=F('total_concluidos'),  # Todos os serviços concluídos
        faturamento='nao'  # Filtro para apenas ordens de serviço com faturamento "não"
    )
    cobrancas_imediatas = OrdemServico.objects.filter(cobranca_imediata = 'sim', faturamento='nao')

    # Calcula valores e contagens
    valor_total_concluidas = para_faturar.aggregate(Sum('valor'))['valor__sum'] or 0
    valor_total_para_faturar = para_faturar.aggregate(Sum('valor'))['valor__sum'] or 0


    contagem_concluidas = para_faturar.count()
    contagem_para_faturar = para_faturar.count()
    contagem_cobrancas_imediatas = cobrancas_imediatas.count()

    context = {
        'para_faturar': para_faturar,
        'valor_total_concluidas': valor_total_concluidas,
        'valor_total_para_faturar': valor_total_para_faturar,
        'contagem_concluidas': contagem_concluidas,
        'contagem_para_faturar': contagem_para_faturar,
        'form': form,
        'cobrancas_imediatas': cobrancas_imediatas,
        'contagem_cobrancas_imediatas': contagem_cobrancas_imediatas,
    }

    return render(request, 'ordemServico/financeiro.html', context)