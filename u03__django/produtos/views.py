from django.shortcuts import render, get_object_or_404
from .models import Produto

def produtos(request):
    PRODUTOS = Produto.objects.all()
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)

def produto_detalhe(request, id):
    # produto = Produto.objects.get(id=id)
    # MELHOR PRÁTICA: Substitui o .get() e protege o site contra links errados
    produto = get_object_or_404(Produto, id=id)
    return render(request, "produtos/produto_detalhe.html", {"produto": produto})

def produtos_esgotados(request):
    produtis = produtos,object.filter(
        estoque=0
    )
    return render(request, "produtos/produtos.html",
    {
        "produtos": produtos
    })

