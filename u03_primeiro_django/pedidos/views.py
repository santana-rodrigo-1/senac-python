from django.shortcuts import get_object_or_404, redirect, render
from produtos.models import Produto

def ver_carrinho(request):
    """Exibe o conteúdo atual do carrinho de compras."""
    carrinho = request.session.get("carrinho", {})
    produtos_no_carrinho = []
    total_geral = 0

    for id_produto, item_data in carrinho.items():
        # Se você salvou apenas a quantidade, ou um dicionário, tratamos aqui:
        quantidade = item_data.get("quantidade", 1) if isinstance(item_data, dict) else item_data

        produto = get_object_or_404(Produto, id=id_produto)
        subtotal = produto.preco * quantidade
        total_geral += subtotal

        produtos_no_carrinho.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": subtotal
        })

    contexto = {
        "produtos": produtos_no_carrinho,
        "total_geral": total_geral,
    }
    return render(request, "pedidos/carrinho.html", contexto)


def adicionar_carrinho(request, id):
    """Adiciona um produto ou incrementa sua quantidade no carrinho."""
    # Garante que o produto existe antes de mexer na sessão
    produto = get_object_or_404(Produto, id=id)
    carrinho = request.session.get("carrinho", {})
    
    id_str = str(id)

    if id_str in carrinho:
        # Se já for um dicionário ou inteiro, tratamos a quantidade
        if isinstance(carrinho[id_str], dict):
            carrinho[id_str]["quantidade"] += 1
        else:
            carrinho[id_str] = {"quantidade": carrinho[id_str] + 1}
    else:
        carrinho[id_str] = {
            "nome": produto.nome,
            "preco": str(produto.preco),
            "quantidade": 1,
        }

    request.session["carrinho"] = carrinho
    # Marca a sessão como modificada para garantir que o Django salve as alterações
    request.session.modified = True 
    
    return redirect("carrinho")  # Certifique-se de que o name da URL é "carrinho"



'''
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
'''