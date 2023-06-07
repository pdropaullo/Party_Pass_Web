from django.shortcuts import render, redirect, get_object_or_404
from .models import Comandas
from .models import Clientes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/index.html', {'comandas': comandas})

def recarregar_comanda(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/recarregar_comanda.html', {'comandas': comandas})

def realizar_consumo(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/realizar_consumo.html', {'comandas': comandas})

def ferramentas(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/ferramentas.html', {'comandas': comandas})

def sobre(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/sobre.html', {'comandas': comandas})

def pesquisar_cliente(request):
    clientes = Clientes.objects.filter().order_by('-id')   
    return render(request, 'pages/recarregar_comanda.html', {'clientes':clientes})

def search(request): 
    cliente_id = request.GET.get('search')
    clientes = get_object_or_404(Clientes, id=cliente_id)
    return render(request, 'pages/recarregar_comanda.html', {'clientes':clientes})
