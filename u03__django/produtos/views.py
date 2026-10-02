from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produto, Categoria
from .forms import ProdutoForm

def produtos(request):
    PRODUTOS = Produto.objects.all()
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)

def produto_detalhe(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, "produtos/produto_detalhe.html", {"produto": produto})

def produtos_esgotados(request):
    # Busca apenas os tênis cujo estoque cadastrado no admin seja igual a 0
    lista_esgotados = Produto.objects.filter(estoque=0)
    contexto = {
        "produtos": lista_esgotados
    }
    return render(request, "produtos/produtos.html", contexto)

def produtos_categoria(request, categoria):
    # CORREÇÃO: Buscando os produtos usando o relacionamento correto do Django (__nome__iexact)
    produtos_filtrados = Produto.objects.filter(categoria__nome__iexact=categoria)
    
    return render(request, "produtos/produtos.html", {
        "produtos": produtos_filtrados,
        "categoria_nome": categoria
    })

@login_required
def produto_novo(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Produto cadastrado com sucesso!"
            )
            return redirect("produtos")
    else:
        form = ProdutoForm()

    return render(
        request,
        "produtos/produto_form.html",
        {
            "form": form
        }
    )






'''
from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProdutoForm
from django.shortcuts import render
from .models import Produto, Categoria


def produtos(request):
    PRODUTOS = Produto.objects.all()
    contexto = {
        "produtos": PRODUTOS
    }
    return render(request, "produtos/produtos.html", contexto)

def produto_detalhe(request, id):

    produto = get_object_or_404(Produto, id=id)
    return render(request, "produtos/produto_detalhe.html", {"produto": produto})

def produtos_esgotados(request):
    # Busca apenas os tênis cujo estoque cadastrado no admin seja igual a 0
    lista_esgotados = Produto.objects.filter(estoque=0)
    
    contexto = {
        "produtos": lista_esgotados
    }
    return render(request, "produtos/produtos.html", contexto)

def produtos_categoria(request, categoria):
    produto = Produto.objects.filter(
        categoria = categoria
    )
    return render(request, "produtos/produtos.html",{
    "produtos":produto
    })

@login_required
def produto_novo(request):

    if request.method == "POST":

        form = ProdutoForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Produto cadastrado com sucesso!"
            )

            return redirect("produtos")

    else:

        form = ProdutoForm()

    return render(
        request,
        "produtos/produto_form.html",
        {
            "form": form
        }
    )
'''