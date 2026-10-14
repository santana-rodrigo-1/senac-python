from django.shortcuts import get_object_or_404, redirect, render
from u03.u03a16.u03_primeiro_django.produtos.models import Produto

def carrinho(request):
    carrinho_sessao = request.session.get("carrinho", {})

    produtos = []
    total_geral = 0

    for id_produto, item_data in carrinho_sessao.items():
        # Como o item é um dicionário, extraímos a quantidade de dentro dele com segurança
        if isinstance(item_data, dict):
            quantidade = item_data.get("quantidade", 1)
        else:
            quantidade = item_data

        produto = get_object_or_404(Produto, id=id_produto)
        
        subtotal = produto.preco * quantidade 
        total_geral += subtotal

        produtos.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": subtotal
        })

    return render(
        request,
        "pedidos/carrinho.html",
        {
            "produtos": produtos,
            "total_geral": total_geral  # Nome exato que o seu HTML espera
        }
    )


def adicionar_carrinho(request, id):
    produto = get_object_or_404(Produto, id=id)
    carrinho_sessao = request.session.get("carrinho", {})

    if str(id) in carrinho_sessao:
        if isinstance(carrinho_sessao[str(id)], dict):
            carrinho_sessao[str(id)]["quantidade"] += 1
        else:
            carrinho_sessao[str(id)] = {"quantidade": carrinho_sessao[str(id)] + 1}
    else:
        carrinho_sessao[str(id)] = {
            "nome": produto.nome,
            "preco": str(produto.preco),
            "quantidade": 1,
        }

    request.session["carrinho"] = carrinho_sessao
    return redirect("carrinho")


def ver_carrinho(request):
    # Faz com que a rota de ver o carrinho chame a lógica completa de cálculo
    return carrinho(request)



def contador_carrinho(request):
    carrinho_sessao = request.session.get("carrinho", {})
    
    # Soma a quantidade de itens salvos na sessão (exemplo comum)
    quantidade_total = sum(item.get('quantidade', 0) for item in carrinho_sessao.values())
    
    # Retorna um dicionário (o Django exige isso de um context processor)
    return {
        "carrinho": carrinho_sessao,
        "quantidade_carrinho": quantidade_total,
    }

def remover_carrinho(request, id):
    """Diminui em 1 a quantidade do produto no carrinho."""
    carrinho = request.session.get("carrinho", {})
    id_produto = str(id)

    if id_produto in carrinho:
        if isinstance(carrinho[id_produto], dict):
            carrinho[id_produto]["quantidade"] -= 1
            if carrinho[id_produto]["quantidade"] <= 0:
                del carrinho[id_produto]
        else:
            carrinho[id_produto] -= 1
            if carrinho[id_produto] <= 0:
                del carrinho[id_produto]

    request.session["carrinho"] = carrinho
    request.session.modified = True
    return redirect("carrinho")


def excluir_carrinho(request, id):
    """Remove o item por completo do carrinho."""
    carrinho = request.session.get("carrinho", {})
    id_produto = str(id)

    if id_produto in carrinho:
        del carrinho[id_produto]

    request.session["carrinho"] = carrinho
    request.session.modified = True
    return redirect("carrinho")