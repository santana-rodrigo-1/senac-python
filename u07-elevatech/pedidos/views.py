from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db import transaction
from produtos.models import Elevador
from .models import Pedido, ItemPedido

@require_POST
def adicionar(request, pk):
    # Verifica se o elevador existe
    get_object_or_404(Elevador, pk=pk)
    
    # Pega o carrinho da sessão (ou cria um vazio se não existir)
    carrinho = request.session.get("carrinho", {})
    chave = str(pk)
    
    # Adiciona +1 na quantidade
    carrinho[chave] = carrinho.get(chave, 0) + 1
    
    # Salva de volta na sessão
    request.session["carrinho"] = carrinho
    
    return redirect("ver_carrinho")

def ver_carrinho(request):
    carrinho = request.session.get("carrinho", {})
    itens = []
    total = 0
    
    # Transforma o dicionário {id: qtd} em uma lista de objetos reais
    for pk, qtd in carrinho.items():
        elevador = Elevador.objects.filter(pk=pk).first()
        if elevador:
            subtotal = elevador.preco * qtd
            total += subtotal
            itens.append({
                "elevador": elevador,
                "quantidade": qtd,
                "subtotal": subtotal
            })

    return render(request, "pedidos/carrinho.html", {"itens": itens, "total": total})

@login_required
def finalizar(request):
    carrinho = request.session.get("carrinho", {})
    if not carrinho:
        return redirect("catalogo")

    # Cria o Pedido com transação (Fase 9 do manual)
    with transaction.atomic():
        pedido = Pedido.objects.create(usuario=request.user)
        for pk, qtd in carrinho.items():
            elevador = get_object_or_404(Elevador, pk=pk)
            ItemPedido.objects.create(
                pedido=pedido,
                elevador=elevador,
                quantidade=qtd,
                preco=elevador.preco,
            )
            # Baixa no estoque
            elevador.estoque -= qtd
            elevador.save()

    # Limpa o carrinho
    request.session["carrinho"] = {}
    return redirect("meus_pedidos")

@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by("-criado_em")
    return render(request, "pedidos/meus_pedidos.html", {"pedidos": pedidos})