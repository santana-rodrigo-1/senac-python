from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Elevador, SolicitacaoOrcamento
from .forms import OrcamentoForm


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
            solicitacao = form.save()
            return render(
                request,
                "produtos/orcamento_sucesso.html",
                {"solicitacao": solicitacao},
            )
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
