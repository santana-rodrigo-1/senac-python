from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Elevador
from .forms import ElevadorForm


@login_required
def painel(request):
    # request.user é o usuário logado
    return render(request, "core/painel.html", {"usuario": request.user})


def lista_elevadores(request):
    # só elevadores ativos, ordenados por nome
    elevadores = Elevador.objects.filter(ativo=True).order_by("nome")

    # busca opcional pela caixa de pesquisa (?q=...)
    termo = request.GET.get("q")
    if termo:
        elevadores = elevadores.filter(nome__icontains=termo)

    return render(request, "produtos/lista.html", {"elevadores": elevadores})


def eh_equipe(user):
    return user.is_staff


@login_required
@user_passes_test(eh_equipe)
def elevador_novo(request):
    if request.method == "POST":
        form = ElevadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("elevadores")
    else:
        form = ElevadorForm()
    return render(request, "produtos/form.html", {"form": form})


@login_required
@user_passes_test(eh_equipe)
def elevador_editar(request, pk):
    elevador = get_object_or_404(Elevador, pk=pk)
    form = ElevadorForm(request.POST or None, request.FILES or None, instance=elevador)
    if form.is_valid():
        form.save()
        return redirect("elevadores")
    return render(request, "produtos/form.html", {"form": form})