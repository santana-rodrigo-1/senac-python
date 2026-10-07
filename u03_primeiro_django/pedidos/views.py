from django.shortcuts import get_object_or_404, redirect, render
from produtos.models import Produto

def carrinho(request):

    carrinho = request.session.get(
        "carrinho",
        {}
    )

    produtos = []

    for id_produto, quantidade in carrinho.items():

        produto = get_object_or_404(
            Produto,
            id=id_produto
        )

        produtos.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": produto.preco * quantidade
        })

    return render(
        request,
        "pedidos/carrinho.html",
        {
            "produtos": produtos
        }
    )


def adicionar_carrinho(request, id):
    produto = get_object_or_404(Produto, id=id)
    carrinho = request.session.get("carrinho", {})

    if str(id) in carrinho:
        carrinho[str(id)]["quantidade"] += 1
    else:
        carrinho[str(id)] = {
            "nome": produto.nome,
            "preco": str(produto.preco),
            "quantidade": 1,
        }

    request.session["carrinho"] = carrinho
    return redirect("carrinho")


def ver_carrinho(request):
    carrinho = request.session.get("carrinho", {})
    return render(request, "pedidos/carrinho.html", {"carrinho": carrinho})