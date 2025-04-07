from django.shortcuts import render
from django.core.paginator import Paginator
from veiculos.models import Carro
from django.contrib.auth.decorators import login_required

def home_view(request):
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
        from django.db.models import Q
        carros = carros.filter(Q(marca__icontains=marca) | Q(modelo__icontains=marca))

    paginator = Paginator(carros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'veiculos/home.html', {'page_obj': page_obj})
    carros = Carro.objects.filter(disponivel=True)

    paginator = Paginator(carros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'veiculos/carros_disponiveis.html', {'page_obj': page_obj})

    @login_required(login_url='/login/')
    def home_view(request):
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
      return render(request, 'veiculos/home.html', {'page_obj': page_obj})
