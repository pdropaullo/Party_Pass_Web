from django.shortcuts import render, redirect, get_object_or_404
from .models import Comandas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clientes.models import Clientes
from datetime import date
from produtos.models import Produtos
from django.http import JsonResponse

def index(request):
    comandas = Comandas.objects.all()
    return render(request, 'pages/index.html', {'comandas': comandas})


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
    q = request.GET.get('busca_com')
    produto_id = request.GET.get('produto_id')
    quantidade = request.GET.get('quantidade')

    if q and produto_id and quantidade is not None:
        cliente = get_object_or_404(Clientes, id=q)
        comanda = get_object_or_404(Comandas, id=q)
        produto = get_object_or_404(Produtos, id=produto_id)

        if cliente and comanda and produto:
            return redirect('realizar_consumo', cliente_id=cliente.id, comanda_id=comanda.id, produto_id=produto.id, quantidade=quantidade)

    return render(request, 'pages/error.html')


def realizar_consumo(request, cliente_id, comanda_id, produto_id, quantidade):
    # Verificar se o cliente, comanda e produto existem
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    comanda = get_object_or_404(Comandas, pk=comanda_id, cliente=cliente)
    produto = get_object_or_404(Produtos, pk=produto_id)

    try:
        quantidade = int(quantidade)

        if quantidade <= 0:
            # Quantidade inválida (zero ou negativa)
            return JsonResponse({'status': 'error', 'message': 'Quantidade inválida.'})

        if comanda.saldo >= produto.valor * quantidade:
            # Calcular o valor total do consumo
            valor_total = produto.valor * quantidade

            # Atualizar o saldo da comanda
            comanda.saldo -= valor_total
            comanda.save()

            # Retornar uma resposta JSON indicando sucesso
            return JsonResponse({'status': 'success', 'message': 'Consumo realizado com sucesso.'})

        # Saldo insuficiente na comanda
        return JsonResponse({'status': 'error', 'message': 'Saldo insuficiente na comanda.'})

    except ValueError:
        # Quantidade inválida (não é um número inteiro)
        return JsonResponse({'status': 'error', 'message': 'Quantidade inválida.'})

    # Verificar se o cliente, comanda e produto existem
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    comanda = get_object_or_404(Comandas, pk=comanda_id, cliente=cliente)
    produto = get_object_or_404(Produtos, pk=produto_id)

    # Obter a quantidade a ser consumida

    quantidade = int(request.GET.get('quantidade'))

    # Verificar se o saldo da comanda é suficiente para o consumo
    if comanda.saldo >= produto.valor * quantidade:
        # Calcular o valor total do consumo
        valor_total = produto.valor * quantidade

        # Atualizar o saldo da comanda
        comanda.saldo -= valor_total
        comanda.save()

        # Retornar uma resposta JSON indicando sucesso
        return JsonResponse({'status': 'success', 'message': 'Consumo realizado com sucesso.'})
    else:
        # Retornar uma resposta JSON indicando erro de saldo insuficiente
        return JsonResponse({'status': 'error', 'message': 'Saldo insuficiente na comanda.'})



# def busca_prod(request):
#     produtos = Produtos.objects.all()
#     data = [{'id': produto.id, 'nome': produto.nome, 'valor': produto.valor} for produto in produtos]
#     return JsonResponse(data, safe=False)

# def realizar_consumo(request):
#     comandas = Comandas.objects.all()
#     return render(request, 'pages/realizar_consumo.html', {'comandas': comandas})

def busca_prod(request):
    busca_prod_id = request.GET.get('busca_prod')
    produto = get_object_or_404(Produtos, id=busca_prod_id)
    data = {'id': produto.id, 'nome': produto.nome, 'valor': produto.valor}
    return JsonResponse(data, safe=False)

