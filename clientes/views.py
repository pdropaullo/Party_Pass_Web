from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import Clientes
from comandas.models import Comandas
from datetime import date
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def cadastrar_cliente(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    if request.method == "POST":
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")
        if telefone == "":
            return HttpResponse("O campo Telefone é obrigatório.")
        email = request.POST.get("email")
        data_nascimento = request.POST.get("data_nascimento")
        endereco = request.POST.get("endereco")
        saldo = request.POST.get("saldo")
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
        return render(request, "pages/cadastrar_cliente.html", {"comandas": comandas})


@login_required(redirect_field_name="login")
def pesquisar_cliente(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    busca = request.GET.get("pesquisar_cliente")
    clientes = Clientes.objects.filter().order_by("-id")

    if busca:
        clientes = Clientes.objects.filter(
            Q(nome__icontains=busca) | Q(cpf__icontains=busca)
        )

    paginator = Paginator(clientes, 5)  # Exibe 5 registros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "pages/pesquisar_cliente.html",
        {"clientes": page_obj, "comandas": comandas},
    )
