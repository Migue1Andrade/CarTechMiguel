from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from veiculos.models import Carro
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.db.models import Q

def get_home_context(request):
    carros = Carro.objects.filter(disponivel=True)

    preco = request.GET.get('preco')
    if preco:
        try:
            preco = float(preco)
            carros = carros.filter(valor__lte=preco)
        except ValueError:
            pass

    tipo = request.GET.get('tipo')
    if tipo and tipo != 'all':
        carros = carros.filter(tipo_combustivel=tipo)

    cor = request.GET.get('cor')
    if cor:
        carros = carros.filter(cor__icontains=cor)

    km = request.GET.get('km')
    if km:
        try:
            km = int(km)
            carros = carros.filter(quilometragem__gte=km)
        except ValueError:
            pass

    marca = request.GET.get('marca')
    if marca:
        carros = carros.filter(Q(marca__icontains=marca) | Q(modelo__icontains=marca))

    paginator = Paginator(carros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return {
        'page_obj': page_obj
    }

@login_required(login_url='/login/')
def home_view(request):
    context = get_home_context(request)
    return render(request, 'veiculos/home.html', context)

@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        context = get_home_context(request)
        context.update({
            'abrir_modal': True,
            'nome': nome,
            'email': email,
        })

        if new_password != confirm_password:
            messages.error(request, "A nova senha e a confirmação não coincidem.")
            return render(request, 'veiculos/home.html', context)

        if not user.check_password(old_password):
            messages.error(request, "Sua senha atual está incorreta.")
            return render(request, 'veiculos/home.html', context)

        user.nome = nome
        user.email = email

        if new_password:
            user.set_password(new_password)

        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Seu perfil foi atualizado com sucesso!")
        return redirect('home')

    return redirect('home')
