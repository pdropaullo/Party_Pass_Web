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
    produtos = Produtos.objects.filter().order_by('-id')   
    return render(request, 'pages/pesquisar_produtos.html', {'produtos':produtos})

def search(request): 
    filtro = request.GET.get('filtro', 'codigo')  # Obtém o valor do filtro selecionado ou define 'codigo' como padrão
    q = request.GET.get('search', '')

    if filtro == 'codigo':
        produtos = Produtos.objects.filter(id__icontains=q).order_by('-id')
    elif filtro == 'nome':
        produtos = Produtos.objects.filter(nome__icontains=q).order_by('-id')
    elif filtro == 'categoria':
        produtos = Produtos.objects.filter(categoria__icontains=q).order_by('-id')
    
    return render(request, 'pages/pesquisar_produtos.html', {'produtos': produtos})

