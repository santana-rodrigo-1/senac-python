from django.shortcuts import render
PRODUTOS =[
    {
        "id": 1,
        "nome": "Air Run",
        "preco": 299.90,
        "descricao": "Tênis confortável para corrida.",
        "categoria": "Corrida",
        "estoque": 10,
        "imagem": "core/images/air-run.jpg"
    },
    {
        "id": 2,
        "nome": "Street Max",
        "preco": 399.90,
        "descricao": "Tênis urbano para o dia a dia.",
        "categoria": "Streetwear",
        "estoque": 5,
        "imagem": "core/images/street-max.jpg"
    },
    {
        "id": 3,
        "nome": "Runner Pro",
        "preco": 499.90,
        "descricao": "Tênis profissional.",
        "categoria": "Corrida",
        "estoque": 0,
        "imagem": "core/images/runner-pro.jpg"

    },
]


def produtos(request):
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)
def produto_detalhe(request, id):
    produto = None
    
    for item in PRODUTOS :
        if item["id"] == id:
            produto = item
            break
    return render(request, "produtos/produto_detalhe.html",{"produto": produto})

