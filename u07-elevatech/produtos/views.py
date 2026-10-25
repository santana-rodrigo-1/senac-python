from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Elevador
from .forms import ElevadorForm

# Catálogo Público
def lista_elevadores(request):
    elevadores = Elevador.objects.filter(ativo=True).order_by("nome")
    termo = request.GET.get("q")
    if termo:
        elevadores = elevadores.filter(nome__icontains=termo)
    return render(request, "produtos/lista.html", {"elevadores": elevadores})

# Permissão (Só a equipe acessa)
def eh_staff(user):
    return user.is_staff

# Painel Administrativo
@login_required
@user_passes_test(eh_staff)
def painel(request):
    elevadores = Elevador.objects.all().order_by("nome")
    return render(request, "produtos/painel.html", {"elevadores": elevadores})

@login_required
@user_passes_test(eh_staff)
def elevador_novo(request):
    if request.method == "POST":
        form = ElevadorForm(request.POST, request.FILES) # request.FILES para imagens
        if form.is_valid():
            form.save()
            return redirect("painel")
    else:
        form = ElevadorForm()
    return render(request, "produtos/form_elevador.html", {"form": form})

@login_required
@user_passes_test(eh_staff)
def elevador_editar(request, pk):
    elevador = get_object_or_404(Elevador, pk=pk)
    if request.method == "POST":
        form = ElevadorForm(request.POST, request.FILES, instance=elevador)
        if form.is_valid():
            form.save()
            return redirect("painel")
    else:
        form = ElevadorForm(instance=elevador)
    return render(request, "produtos/form_elevador.html", {"form": form})

@login_required
@user_passes_test(eh_staff)
def elevador_excluir(request, pk):
    elevador = get_object_or_404(Elevador, pk=pk)
    elevador.delete()
    return redirect("painel")
