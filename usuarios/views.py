from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email ou senha inválidos.')

    return render(request, 'usuarios/login.html')

def register_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if senha != senha2:
            messages.error(request, "As senhas não conferem!")
            return render(request, 'usuarios/register.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Esse email já está cadastrado!")
            return render(request, 'usuarios/register.html')

        try:
            usuario = Usuario.objects.create_user(email=email, nome=nome, senha=senha)
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Erro ao criar usuário: {e}")
            return render(request, 'usuarios/register.html')

    return render(request, 'usuarios/register.html')
