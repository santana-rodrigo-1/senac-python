from django.shortcuts import render
from .models import Produto



def produtos(request):
    PRODUTOS = Produto.objects.all()
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)
def produto_detalhe(request, id):
    produto = Produto.object.get(id=id)
    
    for item in PRODUTOS :
        if item["id"] == id:
            produto = item
            break
    return render(request, "produtos/produto_detalhe.html",{"produto": produto})