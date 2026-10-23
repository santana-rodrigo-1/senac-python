from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.mail import send_mail  # <-- IMPORT ADICIONADO

from .models import Categoria, Elevador, SolicitacaoOrcamento, Pedido, ItemPedido
from .forms import OrcamentoForm, ElevadorForm, CheckoutForm
from . import carrinho as cart

# =============================================================
# Catálogo e Detalhes
# =============================================================

def catalogo(request):
    elevadores = Elevador.objects.filter(ativo=True)
    todos_nomes = Elevador.objects.filter(ativo=True).values_list("nome", flat=True).order_by("nome")

    tipo = request.GET.get("tipo", "").strip()
    categoria_slug = request.GET.get("categoria", "").strip()
    busca = request.GET.get("q", "").strip()

    if tipo:
        elevadores = elevadores.filter(tipo=tipo)
    if categoria_slug:
        elevadores = elevadores.filter(categoria__slug=categoria_slug)
    if busca:
        elevadores = elevadores.filter(
            Q(nome__icontains=busca) | Q(descricao_curta__icontains=busca)
        )

    return render(request, "produtos/catalogo.html", {
        "elevadores": elevadores,
        "categorias": Categoria.objects.all(),
        "tipos": Elevador.Tipo.choices,
        "todos_nomes": todos_nomes,
        "tipo_atual": tipo,
        "categoria_atual": categoria_slug,
        "busca": busca,
    })


def detalhe(request, slug):
    elevador = get_object_or_404(Elevador, slug=slug, ativo=True)
    relacionados = (
        Elevador.objects.filter(ativo=True, categoria=elevador.categoria)
        .exclude(pk=elevador.pk)[:3]
    )
    return render(request, "produtos/detalhe.html", {
        "elevador": elevador,
        "relacionados": relacionados,
    })

# =============================================================
# Orçamento
# =============================================================

def orcamento(request):
    if request.method == "POST":
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            if request.user.is_authenticated:
                solicitacao.usuario = request.user
            solicitacao.save()

            # --- INÍCIO DO E-MAIL DE ORÇAMENTO ---
            send_mail(
                f"[ElevaTech] Novo Orçamento #{solicitacao.pk}",
                f"Cliente: {solicitacao.nome}\nE-mail: {solicitacao.email}\nTelefone: {solicitacao.telefone}\nCidade: {solicitacao.cidade}\nPavimentos: {solicitacao.pavimentos}\nMensagem: {solicitacao.mensagem}",
                'contato@elevatech.com.br',
                ['vendas@elevatech.com.br'],
                fail_silently=True,
            )
            # --- FIM DO E-MAIL DE ORÇAMENTO ---

            messages.success(
                request,
                f"Orçamento #{solicitacao.pk} enviado! "
                f"Entraremos em contato em até 1 dia útil."
            )
            return redirect("catalogo")

        messages.error(request, "Verifique os campos destacados em vermelho.")
    else:
        elevador_pk = request.GET.get("elevador")
        initial = {}
        if elevador_pk:
            try:
                initial["elevador"] = int(elevador_pk)
            except (TypeError, ValueError):
                pass
        form = OrcamentoForm(initial=initial)

    return render(request, "produtos/orcamento.html", {"form": form})

# =============================================================
# Carrinho
# =============================================================

def carrinho_ver(request):
    return render(request, "produtos/carrinho.html", {
        "itens": cart.itens(request),
        "total": cart.total(request),
    })


def carrinho_adicionar(request, pk):
    elevador = get_object_or_404(Elevador, pk=pk, ativo=True)
    qtd = request.POST.get("quantidade", 1)
    try:
        qtd = max(1, int(qtd))
    except (TypeError, ValueError):
        qtd = 1
    cart.adicionar(request, pk, qtd)
    messages.success(
        request,
        f"{qtd}x {elevador.nome} adicionado ao carrinho."
    )
    return redirect("carrinho_ver")


def carrinho_atualizar(request, pk):
    if request.method == "POST":
        cart.atualizar(request, pk, request.POST.get("quantidade", 1))
        messages.success(request, "Carrinho atualizado.")
    return redirect("carrinho_ver")


def carrinho_remover(request, pk):
    if request.method == "POST":
        cart.remover(request, pk)
        messages.success(request, "Item removido do carrinho.")
    return redirect("carrinho_ver")

# =============================================================
# Checkout e Pedidos
# =============================================================

@login_required
def checkout(request):
    itens = cart.itens(request)
    if not itens:
        messages.error(request, "Seu carrinho está vazio.")
        return redirect("carrinho_ver")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                pedido = form.save(commit=False)
                pedido.usuario = request.user
                pedido.save()

                for item in itens:
                    ItemPedido.objects.create(
                        pedido=pedido,
                        elevador=item["elevador"],
                        quantidade=item["quantidade"],
                        preco_unitario=item["elevador"].preco,
                    )

            # --- INÍCIO DO E-MAIL DE PEDIDO ---
            send_mail(
                f"[ElevaTech] Novo Pedido #{pedido.pk}",
                f"Cliente: {pedido.nome}\nE-mail: {pedido.email}\nTelefone: {pedido.telefone}\nTotal: R$ {pedido.total:.2f}",
                'contato@elevatech.com.br',
                ['vendas@elevatech.com.br'],
                fail_silently=True,
            )
            # --- FIM DO E-MAIL DE PEDIDO ---

            cart.limpar(request)
            messages.success(
                request,
                f"Pedido #{pedido.pk} confirmado! Acompanhe o status em 'Meus pedidos'."
            )
            return redirect("meus_pedidos")
    else:
        form = CheckoutForm(initial={
            "nome": request.user.get_full_name() or request.user.username,
            "email": request.user.email,
        })

    return render(request, "produtos/checkout.html", {
        "form": form,
        "itens": itens,
        "total": cart.total(request),
    })


@login_required
def meus_pedidos(request):
    pedidos = (
        Pedido.objects.filter(usuario=request.user)
        .prefetch_related("itens__elevador")
        .order_by("-criado_em")
    )
    return render(request, "produtos/meus_pedidos.html", {"pedidos": pedidos})


@login_required
def pedido_detalhe(request, pk):
    pedido = get_object_or_404(
        Pedido, pk=pk, usuario=request.user
    )
    return render(request, "produtos/pedido_detalhe.html", {"pedido": pedido})

# =============================================================
# Painel de elevadores (Staff)
# =============================================================

@login_required
@user_passes_test(lambda u: u.is_staff)
def painel_lista(request):
    elevadores = Elevador.objects.all().order_by("nome")
    return render(request, "produtos/painel/lista.html", {"elevadores": elevadores})


@login_required
@user_passes_test(lambda u: u.is_staff)
def painel_novo(request):
    if request.method == "POST":
        form = ElevadorForm(request.POST, request.FILES)
        if form.is_valid():
            elevador = form.save()
            messages.success(request, f"Elevador '{elevador.nome}' criado!")
            return redirect("painel_lista")
    else:
        form = ElevadorForm()
    return render(request, "produtos/painel/form.html", {
        "form": form, "modo": "novo",
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def painel_editar(request, slug):
    elevador = get_object_or_404(Elevador, slug=slug)
    if request.method == "POST":
        form = ElevadorForm(request.POST, request.FILES, instance=elevador)
        if form.is_valid():
            form.save()
            messages.success(request, f"Elevador '{elevador.nome}' atualizado!")
            return redirect("painel_lista")
    else:
        form = ElevadorForm(instance=elevador)
    return render(request, "produtos/painel/form.html", {
        "form": form, "modo": "editar", "elevador": elevador,
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def painel_excluir(request, slug):
    elevador = get_object_or_404(Elevador, slug=slug)
    if request.method == "POST":
        nome = elevador.nome
        elevador.delete()
        messages.success(request, f"Elevador '{nome}' excluído.")
        return redirect("painel_lista")
    return render(request, "produtos/painel/confirmar_exclusao.html", {
        "elevador": elevador,
    })