from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import transaction
from produtos.models import Elevador
from .models import Pedido, ItemPedido


@require_POST
def adicionar(request, pk):
    elevador = get_object_or_404(Elevador, pk=pk)
    carrinho = request.session.get("carrinho", {})
    chave = str(pk)
    carrinho[chave] = carrinho.get(chave, 0) + 1
    request.session["carrinho"] = carrinho
    return redirect("ver_carrinho")


def ver_carrinho(request):
    carrinho = request.session.get("carrinho", {})
    itens = []
    total = 0

    for pk, qtd in carrinho.items():
        elevador = Elevador.objects.filter(pk=pk).first()
        if elevador:
            subtotal = elevador.preco * qtd
            total += subtotal
            itens.append(
                {"elevador": elevador, "quantidade": qtd, "subtotal": subtotal}
            )

    return render(request, "pedidos/carrinho.html", {"itens": itens, "total": total})


@login_required
def finalizar(request):
    carrinho = request.session.get("carrinho", {})
    if not carrinho:
        return redirect("catalogo")

    with transaction.atomic():
        pedido = Pedido.objects.create(usuario=request.user)
        for pk, qtd in carrinho.items():
            elevador = Elevador.objects.select_for_update().get(pk=pk)
            ItemPedido.objects.create(
                pedido=pedido,
                elevador=elevador,
                quantidade=qtd,
                preco=elevador.preco,
            )
            elevador.estoque -= qtd
            elevador.save()

    request.session["carrinho"] = {}
    return redirect("meus_pedidos")


@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by("-criado_em")
    return render(request, "pedidos/meus_pedidos.html", {"pedidos": pedidos})


@require_POST
def atualizar_carrinho(request, pk):
    carrinho = request.session.get("carrinho", {})
    chave = str(pk)
    qtd = int(request.POST.get("quantidade", 1))

    if qtd > 0:
        carrinho[chave] = qtd
    else:
        carrinho.pop(chave, None)  # Se for 0, remove

    request.session["carrinho"] = carrinho
    return redirect("ver_carrinho")


def limpar_carrinho(request):
    request.session["carrinho"] = {}
    return redirect("ver_carrinho")
