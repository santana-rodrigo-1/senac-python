from django.shortcuts import render

PRODUTOS =[
    {
        "id": 1,
        "nome": "Air Run",
        "preco": 299.90,
        "descricao": "Tênis confortável para corrida.",
        "categoria": "Corrida",
        "estoque": 10,
        "marca": "marca01"
    },
    {
        "id": 2,
        "nome": "Street Max",
        "preco": 399.90,
        "descricao": "Tênis urbano para o dia a dia.",
        "categoria": "Streetwear",
        "estoque": 5,
        "marca": "marca02"
    },
    {
        "id": 3,
        "nome": "Runner Pro",
        "preco": 499.90,
        "descricao": "Tênis profissional.",
        "categoria": "Corrida",
        "estoque": 0,
        "marca": "marca03"
    },
]


def home(request):
    categorias = [
        "Corrida", 
        "Casual",
        "Esportivo",
        "Streetwear"
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
    
    for item in PRODUTOS :
        if item["id"] == id:
            produto = item
            break
    return render(request, "core/produto_detalhe.html",{"produto": produto})

def contato(request):
    return render(request, "core/contato.html")
