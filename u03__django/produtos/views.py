from django.shortcuts import render, get_object_or_404
from .models import Produto

def produtos(request):
    PRODUTOS = Produto.objects.all()
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "produtos/produto_detalhe.html", {"produto": produto})

def produtos_esgotados(request):
    produtos = produtos,object.filter(
        estoque=0
    )
    return render(request, "produtos/produtos.html",
    {
        "produtos": produtos
    })