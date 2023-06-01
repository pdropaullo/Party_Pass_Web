from django.shortcuts import render, redirect
from .models import Clientes

def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get("Nome")
        cpf = request.POST.get("CPF")
        telefone = request.POST.get("Telefone")
        email = request.POST.get("Email")
        data_nascimento = request.POST.get("Data_nascimento")
        endereco = request.POST.get("Endereço")


        novo_cliente = Clientes(
            nome=nome,
            cpf=cpf,
            telefone=telefone,
        )