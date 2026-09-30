from django.shortcuts import render, get_object_or_404
from .models import Produto

def produtos(request):
    PRODUTOS = Produto.objects.all()
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)

def produto_detalhe(request, id):

    produto = get_object_or_404(Produto, id=id)
    return render(request, "produtos/produto_detalhe.html", {"produto": produto})

def produtos_esgotados(request):
    # Busca apenas os tênis cujo estoque cadastrado no admin seja igual a 0
    lista_esgotados = Produto.objects.filter(estoque=0)
    
    contexto = {
        "produtos": lista_esgotados
    }
    return render(request, "produtos/produtos.html", contexto)
