from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from produtos.models import Elevador
from pedidos.models import Pedido

# Função que verifica se o usuário é da equipe
def eh_equipe(user):
    return user.is_staff

@login_required
@user_passes_test(eh_equipe)
def painel_home(request):
    total_produtos = Elevador.objects.count()
    total_pedidos = Pedido.objects.count()
    pedidos_recentes = Pedido.objects.order_by('-criado_em')[:5]
    
    return render(request, 'dashboard/home.html', {
        'total_produtos': total_produtos,
        'total_pedidos': total_pedidos,
        'pedidos_recentes': pedidos_recentes,
    })

@login_required
@user_passes_test(eh_equipe)
def painel_produtos(request):
    produtos = Elevador.objects.all().order_by('nome')
    return render(request, 'dashboard/produtos.html', {'produtos': produtos})

@login_required
@user_passes_test(eh_equipe)
def painel_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-criado_em')
    return render(request, 'dashboard/pedidos.html', {'pedidos': pedidos})