from django.shortcuts import get_object_or_404, redirect, render
from produtos.models import Produto

def carrinho(request):
    carrinho = request.session.get(
    "carrinho",
{}
)
    return render(
        request, "pedidos/carrinho.html",
        {
            "carrinho":carrinho
        }
    )


def adicionar_carrinho(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
    )

    carrinho = request.session.get(
        "carrinho",
        {}
    )

    id_produto = str(produto.id)

    if id_produto in carrinho:

        carrinho[id_produto] += 1

    else:

        carrinho[id_produto] = 1

    request.session["carrinho"] = carrinho

    return redirect("carrinho")