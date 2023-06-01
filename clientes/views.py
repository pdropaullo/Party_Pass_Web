from django.shortcuts import render, redirect, HttpResponse
from .models import Clientes


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

        novo_cliente = Clientes(
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            email=email,
            data_nascimento=data_nascimento,
            endereco=endereco,
        )
        novo_cliente.save()
        
        return redirect("home")
    else:
        return render(request, "pages/cadastrar_cliente.html")
    
    
def pesquisar_cliente(request):
    busca = request.GET.get("pesquisar_cliente")

    clientes = Clientes.objects.filter(name__icontains=busca)
    return render(request, "pages/index.html", {"clientes": clientes})
