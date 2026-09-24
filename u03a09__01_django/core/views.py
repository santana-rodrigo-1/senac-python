from django.shortcuts import render

PRODUTOS = [
    {
        "id': 1,"
        "mome": "Air Run",
        "preco": 299.90,
        "descricao": "Tênis confortável para corrida.",
        "categoria": "Corrida",
        "estoque": 10

    },
        {
        "id': 2,"
        "mome": "Street MAx",
        "preco": 399.90,
        "descricao": "Tênis urbano par o dia a dia.",
        "categoria": "Strretwear",
        "estoque": 5

    },
        {
        "id': 3,"
        "mome": "Runner Pro",
        "preco": 499.90,
        "descricao": "Tênis profissional.",
        "categoria": "Corrida",
        "estoque": 0

    },

]

def home(request):
    categorias = [
        "Corrida",
        "casual",
        "Esportivo",
        "streetwear"
    ]
    contexto = {
        "titulo": "Os melhores tênis para o seu estilo",
        "subtitulo": "Encontre seu próximo par.",
        "categorias": categorias
    }
    return render(request, "core/home.html", contexto)

def produtos(request):
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "core/produtos.html", contexto)

def sobre(request):
    return render(request, "core/sobre.html")

def produto_detalhe(request, id):
    produto = None

    for item in PRODUTOS:
        if item["id"] == id:
            produto = item
            break
    return render(request, "core/produto_detalhe.html", {})