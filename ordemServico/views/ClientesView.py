from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ordemServico.forms import ClienteForm

@login_required
def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('clientes') 
    else:
        form = ClienteForm()  

    return render(request, 'ordemServico/clientes.html', {'form': form})
