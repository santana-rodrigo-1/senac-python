from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from produtos.models import Elevador, SolicitacaoOrcamento


def home(request):
    destaques = Elevador.objects.filter(ativo=True, destaque=True)[:3]
    return render(request, "core/home.html", {"destaques": destaques})


def sobre(request):
    return render(request, "core/sobre.html")


def register(request):
    """Cadastro de novo cliente."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # loga automaticamente
            messages.success(request, f"Bem-vindo(a), {user.username}!")
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def meus_orcamentos(request):
    """Histórico de orçamentos do cliente logado."""
    orcamentos = (
        SolicitacaoOrcamento.objects.filter(usuario=request.user)
        .select_related("elevador")
        .order_by("-criado_em")
    )
    return render(request, "core/meus_orcamentos.html", {"orcamentos": orcamentos})
