from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def produtos(request):
    return render(request, "core/produtos.html")

def sobre(request):
    return render(request, "core/sobre.html")
