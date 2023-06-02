from django.shortcuts import render, redirect, get_object_or_404
from . models import Produtos
 
def cadastrar_produtos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor').replace(',', '.')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        
        novo_produto = Produtos(nome=nome,valor=valor, categoria=categoria, descricao=descricao)
        novo_produto.save()
        return redirect('home')
    
    else:
        return render(request, 'pages/cadastrar_produtos.html')
    

def pesquisar_produtos(request):
    return render(request, 'pages/pesquisar_produtos.html')