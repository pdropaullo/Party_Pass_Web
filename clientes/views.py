from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import Clientes
from comandas.models import Comandas
from datetime import date


def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get("Nome")
        cpf = request.POST.get("CPF")
        telefone = request.POST.get("Telefone")
        if telefone == '':
            return HttpResponse("O campo Telefone é obrigatório.")
        email = request.POST.get("Email")
        data_nascimento = request.POST.get("Data_nascimento")
        endereco = request.POST.get("Endereço")
        saldo = request.POST.get("Saldo")
        if saldo:
            saldo = float(saldo)  
        else:
            saldo = 0.00  

        novo_cliente = Clientes(
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            email=email,
            data_nascimento=data_nascimento,
            endereco=endereco
        )
                
        nova_comanda = Comandas(
            cliente=novo_cliente,
            ultima_recarga=date.today(),
            saldo=saldo            
        )
        
        novo_cliente.save()
        nova_comanda.save()
        
        return redirect("home")
    else:
        return render(request, "pages/cadastrar_cliente.html")
    
    
def pesquisar_cliente(request):
    busca = request.GET.get("pesquisar_cliente")
    clientes = None

    if busca:
        clientes = Clientes.objects.filter(Q(nome__icontains=busca) | Q(cpf__icontains=busca))

    return render(request, "pages/pesquisar_cliente.html", {"clientes": clientes})
    

    

   


