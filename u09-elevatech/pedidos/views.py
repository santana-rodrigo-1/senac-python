from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (
    require_POST,
)
from produtos.models import Elevador
from .models import ItemPedido, Pedido


@require_POST
def adicionar(request, pk):
    elevador = get_object_or_404(Elevador, pk=pk)
    carrinho = request.session.get("carrinho", {})
    chave = str(pk)

    # Quantidade atual no carrinho + 1 que está tentando adicionar
    quantidade_atual_no_carrinho = carrinho.get(chave, 0)
    nova_quantidade = quantidade_atual_no_carrinho + 1

    # Valida se há estoque suficiente
    if elevador.estoque < nova_quantidade:
        messages.error(
            request,
            f"Desculpe, estoque insuficiente para '{elevador.nome}'. Disponível: {elevador.estoque}.",
        )
    else:
        carrinho[chave] = nova_quantidade
        request.session["carrinho"] = carrinho
        messages.success(request, f"'{elevador.nome}' adicionado ao carrinho!")

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

    # =========================================================
    # MODO DE TESTE (ADMIN): Simula a compra sem afetar o banco
    # =========================================================
    if request.user.is_staff:
        request.session["carrinho"] = {}  # Limpa o carrinho para não travar
        messages.info(
            request,
            "MODO DE TESTE: Compra simulada! O estoque e o banco não foram alterados.",
        )
        return redirect("meus_pedidos")
    # =========================================================

    try:
        with transaction.atomic():
            pedido = Pedido.objects.create(usuario=request.user)
            for pk, qtd in carrinho.items():
                elevador = Elevador.objects.select_for_update().get(pk=pk)

                # Validação final antes de abater do banco
                if elevador.estoque < qtd:
                    messages.error(
                        request,
                        f"Estoque insuficiente para '{elevador.nome}'. Disponível: {elevador.estoque}, Solicitado: {qtd}.",
                    )
                    raise ValueError("Estoque insuficiente")

                ItemPedido.objects.create(
                    pedido=pedido,
                    elevador=elevador,
                    quantidade=qtd,
                    preco=elevador.preco,
                )
                elevador.estoque -= qtd
                elevador.save()

        request.session["carrinho"] = {}
        messages.success(request, "Pedido realizado com sucesso!")
        return redirect("meus_pedidos")

    except ValueError:
        return redirect("ver_carrinho")


@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by("-criado_em")
    return render(request, "pedidos/meus_pedidos.html", {"pedidos": pedidos})


@require_POST
def atualizar_carrinho(request, pk):
    elevador = get_object_or_404(Elevador, pk=pk)
    carrinho = request.session.get("carrinho", {})
    chave = str(pk)

    try:
        qtd = int(request.POST.get("quantidade", 1))
    except (ValueError, TypeError):
        qtd = 1

    if qtd > 0:
        # Valida se a nova quantidade digitada no carrinho ultrapassa o estoque
        if elevador.estoque < qtd:
            messages.error(
                request,
                f"Quantidade solicitada indisponível para '{elevador.nome}'. Estoque máximo: {elevador.estoque}.",
            )
            # PARADA OBRIGATÓRIA AQUI: Evita que salve o valor errado e limpa o fluxo
            return redirect("ver_carrinho")
        else:
            carrinho[chave] = qtd
            messages.success(request, "Carrinho atualizado com sucesso!")
    else:
        carrinho.pop(chave, None)  # Se for 0, remove
        messages.info(request, f"'{elevador.nome}' foi removido do carrinho.")

    request.session["carrinho"] = carrinho
    return redirect("ver_carrinho")


def limpar_carrinho(request):
    request.session["carrinho"] = {}
    messages.info(request, "Carrinho limpo.")
    return redirect("ver_carrinho")
