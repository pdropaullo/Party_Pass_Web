from django.shortcuts import render, redirect, get_object_or_404
from .models import Comandas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clientes.models import Clientes
from datetime import date

def index(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/index.html', {'comandas': comandas})

def realizar_consumo(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/realizar_consumo.html', {'comandas': comandas})

def ferramentas(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/ferramentas.html', {'comandas': comandas})

def sobre(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/sobre.html', {'comandas': comandas})

def search(request): 
    q = request.GET.get('search')
    cliente = None
    comanda = None
    if q and q.isdigit():
        cliente = Clientes.objects.filter(id=q).first
        comanda = Comandas.objects.filter(id=q).first
        return redirect('recarregar_comanda', id=q)
    else:     
        return render(request, 'pages/error.html')

def pesquisar_comanda(request):
    return render(request, 'pages/pesquisar_comanda.html')

def detalhes_comanda(request, id): 
    cliente = get_object_or_404(Clientes, id=id)
    return render(request, 'pages/recarregar_comandas.html', {'cliente': cliente})

def recarregar_comanda(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    comanda = Comandas.objects.filter(cliente_id=id).first()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        saldo = request.POST.get('saldo')
        valor_comanda = request.POST.get('valor_comanda')
        forma_pagamento = request.POST.get('forma_pagamento')
        cliente.nome = nome
        comanda.saldo = saldo
        comanda.ultima_recarga = date.today()
        
        if valor_comanda.isdigit():
            valor_comanda = valor_comanda.replace(',', '.')
            comanda.saldo = comanda.saldo.replace(',', '.')
            valor_comanda = float(valor_comanda)
            comanda.saldo = float(comanda.saldo) + valor_comanda  # Adiciona o valor da recarga ao saldo existente
            comanda.forma_pagamento = forma_pagamento
        
        cliente.save()
        comanda.save()
        return redirect('home')
    
    else:       
        return render(request, 'pages/recarregar_comanda.html', {'cliente': cliente, 'comanda': comanda})
    
def pesquisar_comanda_consumo(request):
    return render(request, 'pages/pesquisar_comanda_consumo.html')
    
def search_id_consumo(request): 
    q = request.GET.get('search')
    cliente = None
    comanda = None
    if q and q.isdigit():
        cliente = Clientes.objects.filter(id=q).first
        comanda = Comandas.objects.filter(id=q).first
        return redirect('realizar_consumo', id=q)
    else:     
        return render(request, 'pages/error.html')
    
def realizar_consumo(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    comanda = Comandas.objects.filter(cliente_id=id).first()
    return render(request, 'pages/realizar_consumo.html', {'cliente': cliente})



