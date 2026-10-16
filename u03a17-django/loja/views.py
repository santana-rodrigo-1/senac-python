from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    contexto = {
        'produtos': produtos,
    }
    return render(request,"loja/index.html", contexto)