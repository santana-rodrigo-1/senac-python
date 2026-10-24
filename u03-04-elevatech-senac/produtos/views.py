from django.shortcuts import render
from .models import Elevador


def lista_elevadores(request):
    # O ORM busca apenas os ativos e ordena pelo nome
    elevadores = Elevador.objects.filter(ativo=True).order_by("nome")

    # Busca opcional (vamos usar o campo 'q' igual o manual ensina)
    termo = request.GET.get("q")
    if termo:
        elevadores = elevadores.filter(nome__icontains=termo)

    return render(request, "produtos/lista.html", {"elevadores": elevadores})
