from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import UserUpdateForm, CustomUserCreationForm
from produtos.models import Elevador, SolicitacaoOrcamento

def home(request):
    destaques = Elevador.objects.filter(ativo=True, destaque=True)[:3]
    return render(request, "core/home.html", {"destaques": destaques})


def sobre(request):
    return render(request, "core/sobre.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) # <-- Usando o novo form aqui
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bem-vindo(a), {user.username}!")
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def meus_orcamentos(request):
    orcamentos = (
        SolicitacaoOrcamento.objects.filter(usuario=request.user)
        .select_related("elevador")
        .order_by("-criado_em")
    )
    return render(request, "core/meus_orcamentos.html", {"orcamentos": orcamentos})


@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Seus dados foram atualizados com sucesso!")
            return redirect("editar_perfil")
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, "core/editar_perfil.html", {"form": form})