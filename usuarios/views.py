from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from usuarios.models import Usuario
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

Usuario = get_user_model()

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email ou senha inválidos.')

    return render(request, 'usuarios/login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '').strip()
        nome = request.POST.get('nome', '').strip()

        if not email or not senha or not nome:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'usuarios/register.html', {'email': email, 'nome': nome})

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Já existe um usuário com este email.')
            return render(request, 'usuarios/register.html', {'email': email, 'nome': nome})

        try:
            user = Usuario.objects.create_user(
                email=email,
                password=senha,
                nome=nome
            )
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao criar usuário: {e}')
            return render(request, 'usuarios/register.html', {'email': email, 'nome': nome})

    return render(request, 'usuarios/register.html')
