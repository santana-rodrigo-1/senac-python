from produtos.carrinho import contexto as carrinho_contexto


def carrinho(request):
    return carrinho_contexto(request)