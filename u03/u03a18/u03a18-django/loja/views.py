from django.shortcuts import render
from .models import Produto
from import

def home(request):
    produtos = Produto.objects.all()
    contexto = {
        'produtos': produtos,
    }
    return render(request,"loja/index.html", contexto)

def produtos(request):
    produtos = Produto.objects.all()
    contexto = {
        'produtos': produtos,
    }
    return render(request,"loja/produtos.html", contexto)