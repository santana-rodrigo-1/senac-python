from django.shortcuts import render
from produtos.models import Produto, Categoria

def home(request):
    PRODUTOS = Produto.objects.all()
    categorias = Categoria.objects.all()

    contexto = {
        "titulo": "Os melhores tênis para o seu estilo",
        "subtitulo": "Encontre seu próximo par.",
        "categorias": categorias,
        "produtos": PRODUTOS
    }
    return render(request, "core/home.html", contexto)

def sobre(request):
    return render(request, "core/sobre.html")

