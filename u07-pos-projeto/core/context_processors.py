def carrinho(request):
    carrinho = request.session.get("carrinho", {})
    quantidade = sum(carrinho.values())
    return {"carrinho_quantidade": quantidade}
