from django.shortcuts import render


def home(request):
    return render(request, "catalogo/index.html")


def escadas(request):
    return render(request, "catalogo/escadas.html")