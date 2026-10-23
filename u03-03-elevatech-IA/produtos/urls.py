from django.urls import path
from . import views

urlpatterns = [
    path("elevadores/", views.catalogo, name="catalogo"),
    path("elevadores/<slug:slug>/", views.detalhe, name="produto_detalhe"),
    path("orcamento/", views.orcamento, name="orcamento"),

    # carrinho
    path("carrinho/", views.carrinho_ver, name="carrinho_ver"),
    path("carrinho/adicionar/<int:pk>/", views.carrinho_adicionar, name="carrinho_adicionar"),
    path("carrinho/atualizar/<int:pk>/", views.carrinho_atualizar, name="carrinho_atualizar"),
    path("carrinho/remover/<int:pk>/", views.carrinho_remover, name="carrinho_remover"),
    path("checkout/", views.checkout, name="checkout"),
    path("meus-pedidos/", views.meus_pedidos, name="meus_pedidos"),
    path("meus-pedidos/<int:pk>/", views.pedido_detalhe, name="pedido_detalhe"),
    path("carrinho/orcamento/", views.carrinho_orcamento, name="carrinho_orcamento"),
    path("carrinho/limpar/", views.carrinho_limpar, name="carrinho_limpar"),

    # painel de elevadores (staff)
    path("painel/elevadores/", views.painel_lista, name="painel_lista"),
    path("painel/elevadores/novo/", views.painel_novo, name="painel_novo"),
    path("painel/elevadores/<slug:slug>/editar/", views.painel_editar, name="painel_editar"),
    path("painel/elevadores/<slug:slug>/excluir/", views.painel_excluir, name="painel_excluir"),
]