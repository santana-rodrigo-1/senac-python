"""
Funções utilitárias para manipular o carrinho guardado em request.session.
Formato: {"<elevador_pk>": <quantidade>, ...}
"""

from .models import Elevador
from .models import SolicitacaoOrcamento, Elevador, Pedido

SESSION_KEY = "carrinho"


def _get(request):
    return request.session.get(SESSION_KEY, {})


def _save(request, data):
    request.session[SESSION_KEY] = data


def adicionar(request, elevador_pk, quantidade=1):
    carrinho = _get(request)
    chave = str(elevador_pk)
    carrinho[chave] = carrinho.get(chave, 0) + int(quantidade)
    _save(request, carrinho)


def atualizar(request, elevador_pk, quantidade):
    carrinho = _get(request)
    chave = str(elevador_pk)
    qtd = int(quantidade)
    if qtd <= 0:
        carrinho.pop(chave, None)
    else:
        carrinho[chave] = qtd
    _save(request, carrinho)


def remover(request, elevador_pk):
    carrinho = _get(request)
    carrinho.pop(str(elevador_pk), None)
    _save(request, carrinho)


def limpar(request):
    request.session[SESSION_KEY] = {}


def itens(request):
    """Retorna lista de dicts enriquecidos com objeto Elevador e subtotal."""
    carrinho = _get(request)
    if not carrinho:
        return []

    ids = [int(k) for k in carrinho.keys()]
    elevadores = {e.pk: e for e in Elevador.objects.filter(pk__in=ids)}

    resultado = []
    for pk_str, qtd in carrinho.items():
        elev = elevadores.get(int(pk_str))
        if not elev:
            continue
        resultado.append(
            {
                "elevador": elev,
                "quantidade": qtd,
                "subtotal": elev.preco * qtd,
            }
        )
    return resultado


def total(request):
    return sum(item["subtotal"] for item in itens(request))


def quantidade_total(request):
    """Número de itens (soma de quantidades), para o badge da navbar."""
    return sum(_get(request).values())


def contexto(request):
    """Retorna contexto pronto para qualquer template (via context processor)."""
    return {
        "carrinho_quantidade": quantidade_total(request),
        "carrinho_total": total(request),
    }
