from django.shortcuts import render, get_object_or_404
from django.utils.formats import number_format
from ordemServico.models import Servico, Profile
from django.contrib.auth.decorators import login_required, user_passes_test

# Função que verifica se o usuário é 'Diretor', 'Administrativo' ou 'Líder Técnico'
def verificar_tipo_usuario(user):
    try:
        return user.profile.role in [1, 2, 3]
    except Profile.DoesNotExist:
        return False


@login_required
@user_passes_test(verificar_tipo_usuario)

def servico(request, id):
    
    servico = get_object_or_404(Servico, id=id)
    servico.ordem_servico.valor_formatado = "R$ {:,.2f}".format(servico.ordem_servico.valor).replace(",", "X").replace(".", ",").replace("X", ".")
    
    context = {
        'servico': servico
    }
    return render(request, 'ordemServico/servico.html', context)