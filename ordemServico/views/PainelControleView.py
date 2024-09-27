from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from ordemServico.models import OrdemServico, Profile, Servico

from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum, Count, Q, F
import locale

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')


def verificar_tipo_usuario(user):
    try:
        return user.profile.role in [1, 2, 3]
    except Profile.DoesNotExist:
        return False

@login_required
@user_passes_test(verificar_tipo_usuario)
def painel_de_controle(request):
    
    '''
        OS CRIADAS POR PERÍODO
    '''
    hoje = timezone.now().date()
    
    # Ordens criadas hoje
    ordens_criadas_hoje = OrdemServico.objects.filter(data_criacao=hoje)
    contagem_ordens_criadas_hoje = ordens_criadas_hoje.count()
    
    # Últimos 7 dias
    sete_dias_atras = hoje - timedelta(days=7)
    ordens_ultimos_7_dias = OrdemServico.objects.filter(data_criacao__gte=sete_dias_atras)
    contagem_ordens_ultimos_7_dias = ordens_ultimos_7_dias.count()

    # Últimos 15 dias
    quinze_dias_atras = hoje - timedelta(days=15)
    ordens_ultimos_15_dias = OrdemServico.objects.filter(data_criacao__gte=quinze_dias_atras)
    contagem_ordens_ultimos_15_dias = ordens_ultimos_15_dias.count()

    # Últimos 30 dias
    trinta_dias_atras = hoje - timedelta(days=30)
    ordens_ultimos_30_dias = OrdemServico.objects.filter(data_criacao__gte=trinta_dias_atras)
    contagem_ordens_ultimos_30_dias = ordens_ultimos_30_dias.count()
    
    '''
        SERVIÇOS POR STATUS
    ''' 
    novos_servicos = Servico.objects.filter(status='em_espera')
    qtd_novos_servicos = novos_servicos.count()

    servicos_em_andamento = Servico.objects.filter(status='em_andamento')
    qtd_servicos_em_andamento = servicos_em_andamento.count()

    servicos_finalizados = Servico.objects.filter(status='concluida')
    qtd_servicos_finalizados = servicos_finalizados.count()

    servicos_para_finalizar = Servico.objects.annotate(
        total_tarefas=Count('tarefa'),
        tarefas_concluidas=Count('tarefa', filter=Q(tarefa__status='concluida'))
    ).filter(
        total_tarefas__gt=0,
        total_tarefas=F('tarefas_concluidas'),
        status='em_andamento'
    )
    qtd_servicos_para_finalizar = servicos_para_finalizar.count()
    
    '''
        FATURAMENTOS
    '''
    futuros_faturamentos = OrdemServico.objects.filter(concluida='nao', faturamento='nao')
    valor_total_futuros_faturamentos = futuros_faturamentos.aggregate(Sum('valor'))['valor__sum'] or 0
    contagem_futuros_faturamentos = futuros_faturamentos.count()
    
   # Faturamento liberados
    para_faturar = OrdemServico.objects.annotate(
        total_servicos=Count('servico'),
        total_concluidos=Count('servico', filter=Q(servico__status='concluida'))
    ).filter(
        Q(total_servicos=F('total_concluidos')) | Q(cobranca_imediata='sim'),  # Todos os serviços concluídos ou cobrança imediata
        faturamento='nao'  # Filtro para apenas ordens de serviço com faturamento "não"
    )
    valor_total_para_faturar = para_faturar.aggregate(Sum('valor'))['valor__sum'] or 0    
    contagem_para_faturar = para_faturar.count()
        
    # Faturadas
    faturadas = OrdemServico.objects.filter(faturamento="sim")
    valor_total_faturadas = faturadas.aggregate(Sum('valor'))['valor__sum'] or 0
    contagem_faturadas = faturadas.count()
    
    # Todos os serviços
    servicos = Servico.objects.all().order_by('-ordem_servico__data_criacao')
    
    context = {      
        'contagem_ordens_criadas_hoje': contagem_ordens_criadas_hoje,
        'contagem_ordens_ultimos_7_dias': contagem_ordens_ultimos_7_dias,
        'contagem_ordens_ultimos_15_dias': contagem_ordens_ultimos_15_dias,
        'contagem_ordens_ultimos_30_dias': contagem_ordens_ultimos_30_dias,
        
        
        'qtd_novos_servicos': qtd_novos_servicos,
        'qtd_servicos_em_andamento': qtd_servicos_em_andamento,
        'qtd_servicos_finalizados': qtd_servicos_finalizados,
        'qtd_servicos_para_finalizar': qtd_servicos_para_finalizar,
        
        
        'faturadas': faturadas,
        'valor_total_faturadas': locale.currency(valor_total_faturadas, grouping=True),
        'contagem_faturadas': contagem_faturadas,
        
        'futuros_faturamentos': futuros_faturamentos,
        'valor_total_futuros_faturamentos': locale.currency(valor_total_futuros_faturamentos, grouping=True),
        'contagem_futuros_faturamentos': contagem_futuros_faturamentos,
        
        'para_faturar': para_faturar,
        'valor_total_para_faturar': locale.currency(valor_total_para_faturar, grouping=True),
        'contagem_para_faturar': contagem_para_faturar,
        
        'servicos': servicos,
    }

    return render(request, 'ordemServico/painel_controle.html', context)