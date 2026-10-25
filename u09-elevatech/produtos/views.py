from django.shortcuts import render
from .models import Elevador


def lista_elevadores(request):
    # Busca os elevadores ativos no banco e ordena por nome
    elevadores = Elevador.objects.filter(ativo=True).order_by("nome")

    # Lógica de busca (opcional)
    termo = request.GET.get("q")
    if termo:
        elevadores = elevadores.filter(nome__icontains=termo)

    return render(request, "produtos/lista.html", {"elevadores": elevadores})
