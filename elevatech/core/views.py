from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import UserUpdateForm, CustomUserCreationForm
from produtos.models import Elevador, SolicitacaoOrcamento

from django.core.mail import send_mail
from .forms import ContatoForm, UserUpdateForm, CustomUserCreationForm

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

def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                f"[ElevaTech] Contato do Site - {nome}",
                f"Mensagem de: {nome} ({email})\n\n{mensagem}",
                'contato@elevatech.com.br',
                ['vendas@elevatech.com.br'],
                fail_silently=True,
            )
            messages.success(request, "Mensagem enviada com sucesso! Retornaremos em breve.")
            return redirect("contato")
    else:
        form = ContatoForm()
    
    return render(request, "core/contato.html", {"form": form})

def faq(request):
    return render(request, "core/faq.html")