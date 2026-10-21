from django.shortcuts import render
from produtos.models import Produto

def home(request):

    produtos = Produto.objects.filter(ativo=True)

    return render(
        request,
        "home.html",
        {
            "produtos": produtos
        }
    )