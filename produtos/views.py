from django.shortcuts import render, redirect, get_object_or_404
from . models import Produtos
 
def cadastrar_produtos(request):
    if request.method == 'POST':
        nome = request.POST.get('title')
        valor = request.POST.get('release_year')
        categoria = request.POST.get('director')
        descricao = request.POST.get('description')
        
        novo_produto = Produtos(nome=nome,valor=valor, categoria=categoria, descricao=descricao)
        novo_produto.save()
        return redirect('home')
    
    else:
        return render(request, 'pages/cadastrar_produtos.html')