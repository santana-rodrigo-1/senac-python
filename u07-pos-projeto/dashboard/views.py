from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db import transaction
from produtos.models import Elevador
from pedidos.models import Pedido
from django.core.mail import send_mail

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


@login_required
@user_passes_test(eh_equipe)
@require_POST
def atualizar_status_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    novo_status = request.POST.get("status")
    
    status_validos = ['novo', 'pago', 'enviado', 'entregue', 'cancelado']

    # PROTEÇÃO: Só executa se o status for válido E diferente do atual
    if novo_status in status_validos and novo_status != pedido.status:
        try:
            with transaction.atomic():
                # Se o admin está cancelando, devolve o estoque
                if novo_status == 'cancelado' and pedido.status != 'cancelado':
                    for item in pedido.itens.all():
                        elevador = Elevador.objects.select_for_update().get(pk=item.elevador.pk)
                        elevador.estoque += item.quantidade
                        elevador.save()
                
                pedido.status = novo_status
                pedido.save()
                
            # --- DISPARO DE E-MAILS ---
            if pedido.usuario.email:
                assunto = f"Atualização do Pedido #{pedido.pk} - ElevaTech"
                mensagem = ""
                
                if novo_status == 'pago':
                    assunto = f"Pagamento Aprovado! Pedido #{pedido.pk} - ElevaTech"
                    mensagem = f"Olá, {pedido.usuario.first_name or pedido.usuario.username},\n\nO pagamento do seu pedido #{pedido.pk} foi confirmado com sucesso! Já estamos preparando os seus elevadores para o envio.\n\nObrigado pela confiança,\nEquipe ElevaTech"
                
                elif novo_status == 'enviado':
                    assunto = f"Seu Pedido #{pedido.pk} foi Enviado! - ElevaTech"
                    mensagem = f"Olá, {pedido.usuario.first_name or pedido.usuario.username},\n\nBoas notícias! O seu pedido #{pedido.pk} acabou de sair do nosso centro de distribuição e está a caminho.\n\nEm breve a nossa equipe entrará em contato para agendar a entrega.\n\nAtenciosamente,\nEquipe ElevaTech"
                
                elif novo_status == 'entregue':
                    assunto = f"Pedido #{pedido.pk} Entregue - ElevaTech"
                    mensagem = f"Olá, {pedido.usuario.first_name or pedido.usuario.username},\n\nO seu pedido #{pedido.pk} foi entregue/instalado com sucesso. Esperamos que a sua experiência com a ElevaTech tenha sido excelente!\n\nQualquer dúvida, estamos à disposição.\n\nAtenciosamente,\nEquipe ElevaTech"
                
                elif novo_status == 'cancelado':
                    assunto = f"Pedido #{pedido.pk} Cancelado - ElevaTech"
                    mensagem = f"Olá, {pedido.usuario.first_name or pedido.usuario.username},\n\nInformamos que o seu pedido #{pedido.pk} foi CANCELADO pela loja ElevaTech.\n\nSe houve algum pagamento, o valor será estornado para a sua conta nos próximos dias.\n\nSe você tiver dúvidas ou quiser saber o motivo do cancelamento, por favor, entre em contato com o nosso suporte.\n\nAtenciosamente,\nEquipe ElevaTech"

                # Se uma das condições acima preencheu a mensagem, envia o e-mail
                if mensagem:
                    send_mail(
                        assunto,
                        mensagem,
                        'contato@elevatech.com.br',
                        [pedido.usuario.email],
                        fail_silently=True
                    )
                
            messages.success(request, f"Status do pedido #{pedido.pk} atualizado para '{novo_status.title()}'.")
        except Exception as e:
            messages.error(request, "Erro ao atualizar o status do pedido.")
    else:
        # Se o admin tentar forçar o mesmo status, cai aqui
        messages.warning(request, f"O pedido #{pedido.pk} já está com o status '{novo_status.title()}'.")
        
    return redirect("painel_pedidos")