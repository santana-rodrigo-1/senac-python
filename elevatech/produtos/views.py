from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Categoria, Elevador, SolicitacaoOrcamento
from .forms import OrcamentoForm, ElevadorForm


def catalogo(request):
    elevadores = Elevador.objects.filter(ativo=True)

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

    return render(
        request,
        "produtos/catalogo.html",
        {
            "elevadores": elevadores,
            "categorias": Categoria.objects.all(),
            "tipos": Elevador.Tipo.choices,
            "tipo_atual": tipo,
            "categoria_atual": categoria_slug,
            "busca": busca,
        },
    )


def detalhe(request, slug):
    elevador = get_object_or_404(Elevador, slug=slug, ativo=True)
    relacionados = Elevador.objects.filter(
        ativo=True, categoria=elevador.categoria
    ).exclude(pk=elevador.pk)[:3]
    return render(
        request,
        "produtos/detalhe.html",
        {
            "elevador": elevador,
            "relacionados": relacionados,
        },
    )


def orcamento(request):
    if request.method == "POST":
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            if request.user.is_authenticated:
                solicitacao.usuario = request.user
            solicitacao.save()
            messages.success(
                request,
                f"Orçamento #{solicitacao.pk} enviado! "
                f"Entraremos em contato em até 1 dia útil.",
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
# Painel de elevadores — só para staff
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
    return render(
        request,
        "produtos/painel/form.html",
        {
            "form": form,
            "modo": "novo",
        },
    )


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
    return render(
        request,
        "produtos/painel/form.html",
        {
            "form": form,
            "modo": "editar",
            "elevador": elevador,
        },
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def painel_excluir(request, slug):
    elevador = get_object_or_404(Elevador, slug=slug)
    if request.method == "POST":
        nome = elevador.nome
        elevador.delete()
        messages.success(request, f"Elevador '{nome}' excluído.")
        return redirect("painel_lista")
    return render(
        request,
        "produtos/painel/confirmar_exclusao.html",
        {
            "elevador": elevador,
        },
    )
