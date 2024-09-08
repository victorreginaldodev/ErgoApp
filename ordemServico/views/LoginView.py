from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# View de login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('criar_ordem_servico')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    return render(request, 'ordemServico/login.html')

# View de logout
def user_logout(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout
