from django.shortcuts import render


def home(request):
    # request = pedido do navegador; render monta a resposta com o template
    return render(request, "core/home.html")


def sobre(request):
    return render(request, "core/sobre.html")
