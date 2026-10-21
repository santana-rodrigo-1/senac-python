from django.shortcuts import render


def carrinho(request):
    return render(request, "pedidos/carrinho.html")


def checkout(request):
    return render(request, "pedidos/checkout.html")