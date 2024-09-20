from django.shortcuts import render, redirect
from ordemServico.forms import ClienteForm

from django.contrib.auth.decorators import login_required, user_passes_test
from ordemServico.models import Profile

# Função que verifica se o usuário é 'Diretor', 'Administrativo' ou 'Líder Técnico'
def verificar_tipo_usuario(user):
    try:
        return user.profile.role in [1, 2, 3]
    except Profile.DoesNotExist:
        return False

@login_required
@user_passes_test(verificar_tipo_usuario)
def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('clientes') 
    else:
        form = ClienteForm()  

    return render(request, 'ordemServico/clientes.html', {'form': form})
