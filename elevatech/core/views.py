from django.shortcuts import render
from produtos.models import Elevador


def home(request):
    destaques = Elevador.objects.filter(ativo=True, destaque=True)[:3]
    return render(request, "core/home.html", {"destaques": destaques})
