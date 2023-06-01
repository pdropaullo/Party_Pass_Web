from django.shortcuts import render, redirect, get_object_or_404
from .models import Comandas
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
