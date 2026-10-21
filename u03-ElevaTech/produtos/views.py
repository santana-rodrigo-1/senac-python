from django.shortcuts import render, get_object_or_404
from .models import Produto


def catalogo(request):

    produtos = Produto.objects.filter(
        ativo=True
    )

    contexto = {
        "produtos": produtos
    }

    return render(
        request,
        "produtos/catalogo.html",
        contexto
    )


def detalhes(request, produto_id):

    produto = get_object_or_404(
        Produto,
        id=produto_id
    )

    contexto = {
        "produto": produto
    }

    return render(
        request,
        "produtos/detalhes.html",
        contexto
    )