from django.shortcuts import render
from django.core.paginator import Paginator
from veiculos.models import Carro

def carros_disponiveis(request):

    carros = Carro.objects.filter(disponivel=True)

    paginator = Paginator(carros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'veiculos/carros_disponiveis.html', {'page_obj': page_obj})

def home_view(request):
    carros = Carro.objects.filter(disponivel=True)
    paginator = Paginator(carros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'veiculos/home.html', {'page_obj': page_obj})
