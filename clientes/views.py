from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import Clientes
from comandas.models import Comandas
from datetime import date
from django.contrib import messages
from django.core.paginator import Paginator


def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get("Nome")
        cpf = request.POST.get("CPF")
        telefone = request.POST.get("Telefone")
        if telefone == "":
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
            endereco=endereco,
        )

        nova_comanda = Comandas(
            cliente=novo_cliente, ultima_recarga=date.today(), saldo=saldo
        )

        novo_cliente.save()
        nova_comanda.save()

        return redirect("home")
    else:
        return render(request, "pages/cadastrar_cliente.html")


# def pesquisar_cliente(request):
def pesquisar_cliente(request):
    busca = request.GET.get("pesquisar_cliente")

    if busca:
        clientes = Clientes.objects.filter(
            Q(nome__icontains=busca) | Q(cpf__icontains=busca)
        ).order_by("-id")
    else:
        clientes = []

    paginator = Paginator(clientes, 5)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "pages/pesquisar_cliente.html", {"clientes": page_obj})

    # busca = request.GET.get("pesquisar_cliente")
    # clientes = Clientes.objects.filter().order_by("-id")

    # if busca:
    #     clientes = Clientes.objects.filter(
    #         Q(nome__icontains=busca) | Q(cpf__icontains=busca)
    #     )

    # paginator = Paginator(clientes, 5)  # Exibe 5 registros por página
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    # return render(request, "pages/pesquisar_cliente.html", {"clientes": page_obj})
