from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

from ordemServico.forms import OrdemServicoForm, ServicoForm
from ordemServico.models import OrdemServico, Servico, Profile

# Função que verifica se o usuário é 'Diretor', 'Administrativo' ou 'Líder Técnico'
def verificar_tipo_usuario(user):
    try:
        return user.profile.role in [1, 2, 3]
    except Profile.DoesNotExist:
        return False


@login_required
@user_passes_test(verificar_tipo_usuario)
def criar_ordem_servico(request):
    if request.method == 'POST':
        ordem_servico_form = OrdemServicoForm(request.POST)
        
        ServicoFormSet = inlineformset_factory(
            OrdemServico,
            Servico,
            form=ServicoForm,
            extra=1
        )
        servico_formset = ServicoFormSet(request.POST)

        if ordem_servico_form.is_valid() and servico_formset.is_valid():
            ordem_servico = ordem_servico_form.save()
            
            servico_formset.instance = ordem_servico
            servico_formset.save()

            return redirect(reverse('criar_ordem_servico'))
        else:
            context = {
                'ordem_servico_form': ordem_servico_form,
                'servico_formset': servico_formset,
            }
            return render(request, 'ordemServico/ordem_servico.html', context)
    else:
        ordem_servico_form = OrdemServicoForm()
        
        ServicoFormSet = inlineformset_factory(
            OrdemServico,
            Servico,
            form=ServicoForm,
            extra=1
        )
        servico_formset = ServicoFormSet()

        context = {
            'ordem_servico_form': ordem_servico_form,
            'servico_formset': servico_formset,
        }
        return render(request, 'ordemServico/ordem_servico.html', context)  