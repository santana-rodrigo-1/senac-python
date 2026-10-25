from django.shortcuts import render
from .models import Elevador

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Elevador
from .forms import ElevadorForm


def lista_elevadores(request):
    # Busca os elevadores ativos no banco e ordena por nome
    elevadores = Elevador.objects.filter(ativo=True).order_by("nome")

    # Lógica de busca (opcional)
    termo = request.GET.get("q")
    if termo:
        elevadores = elevadores.filter(nome__icontains=termo)

    return render(request, "produtos/lista.html", {"elevadores": elevadores})


# Verifica se o usuário é da equipe
def eh_equipe(user):
    return user.is_staff


@login_required
@user_passes_test(eh_equipe)
def elevador_novo(request):
    if request.method == "POST":
        form = ElevadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("catalogo")
    else:
        form = ElevadorForm()
    return render(request, "produtos/form.html", {"form": form})


@login_required
@user_passes_test(eh_equipe)
def elevador_editar(request, pk):
    elevador = get_object_or_404(Elevador, pk=pk)
    if request.method == "POST":
        form = ElevadorForm(request.POST, request.FILES, instance=elevador)
        if form.is_valid():
            form.save()
            return redirect("catalogo")
    else:
        form = ElevadorForm(instance=elevador)
    return render(request, "produtos/form.html", {"form": form})
