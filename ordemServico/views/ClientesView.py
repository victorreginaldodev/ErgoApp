from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ordemServico.models import Cliente

@login_required
def clientes(request):

    clientes = Cliente.objects.all()
    
    contex = {
        'clientes': clientes,
    }

    return render(request, 'ordemServico/clientes.html', contex)