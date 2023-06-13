from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from comandas.models import Comandas


@login_required(redirect_field_name="login")
def cadastrar_produtos(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    if request.method == "POST":
        nome = request.POST.get("nome")
        valor = request.POST.get("valor").replace(",", ".")
        categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")

        novo_produto = Produtos(
            nome=nome, valor=valor, categoria=categoria, descricao=descricao
        )
        novo_produto.save()
        return redirect("home")

    else:
        return render(request, "pages/cadastrar_produtos.html", {"comandas": comandas})


@login_required(redirect_field_name="login")
def pesquisar_produtos(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    produtos = Produtos.objects.filter().order_by("-id")
    paginator = Paginator(produtos, 5)  # Exibe 5 registros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "pages/pesquisar_produtos.html",
        {"produtos": page_obj, "comandas": comandas},
    )


@login_required(redirect_field_name="login")
def search(request):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    filtro = request.GET.get("filtro", "codigo")
    q = request.GET.get("search", "")

    if filtro == "codigo":
        produtos = Produtos.objects.filter(id__icontains=q).order_by("-id")
    elif filtro == "nome":
        produtos = Produtos.objects.filter(nome__icontains=q).order_by("-id")
    elif filtro == "categoria":
        produtos = Produtos.objects.filter(categoria__icontains=q).order_by("-id")

    return render(
        request,
        "pages/pesquisar_produtos.html",
        {"produtos": produtos, "comandas": comandas},
    )


@login_required(redirect_field_name="login")
def detalhes_produtos(request, id):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    produto = get_object_or_404(Produtos, id=id)
    return render(
        request,
        "pages/detalhes_produtos.html",
        {"produto": produto, "comandas": comandas},
    )


@login_required(redirect_field_name="login")
def editar_produtos(request, id):
    comandas = Comandas.objects.filter(usuario_id=request.user.id).order_by("-id")
    produto = Produtos.objects.get(id=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        valor = request.POST.get("valor").replace(",", ".")
        categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")

        produto.nome = nome
        produto.valor = valor
        produto.categoria = categoria
        produto.descricao = descricao

        produto.save()
        return redirect("home")

    else:
        return render(
            request,
            "pages/editar_produtos.html",
            {"produto": produto, "comandas": comandas},
        )


def deletar_produtos(request, id):
    produto = Produtos.objects.get(id=id)
    produto.delete()
    return redirect("home")
