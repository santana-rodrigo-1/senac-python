from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditarPerfilForm, CustomPasswordChangeForm
from .models import Perfil

def home(request):
    return render(request, "core/home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def sobre(request):
    return render(request, "core/sobre.html")

@login_required
def perfil(request):
    # Garante que o usuário tenha um perfil
    Perfil.objects.get_or_create(usuario=request.user)
    return render(request, "core/perfil.html")

@login_required
def editar_perfil(request):
    # Garante que o usuário tenha um perfil e o puxa
    perfil, criado = Perfil.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            # Salva os dados do User (Nome, email)
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            
            # Salva os dados do Perfil (Telefone, endereço)
            form.save()
            messages.success(request, "Seus dados foram atualizados com sucesso!")
            return redirect("perfil")
    else:
        form = EditarPerfilForm(instance=perfil, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })
    
    return render(request, "core/editar_perfil.html", {"form": form})