from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ordemServico.forms import RepositorioForm

@login_required
def repositorio(request):
    if request.method == 'POST':
        form = RepositorioForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('repositorio') 
    else:
        form = RepositorioForm()  

    return render(request, 'ordemServico/repositorio.html', {'form': form})