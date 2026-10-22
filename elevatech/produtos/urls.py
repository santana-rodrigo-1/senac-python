from django.urls import path
from . import views

urlpatterns = [
    path("elevadores/", views.catalogo, name="catalogo"),
    path("elevadores/<slug:slug>/", views.detalhe, name="produto_detalhe"),
    path("orcamento/", views.orcamento, name="orcamento"),

    # painel de elevadores (staff)
    path("painel/elevadores/", views.painel_lista, name="painel_lista"),
    path("painel/elevadores/novo/", views.painel_novo, name="painel_novo"),
    path("painel/elevadores/<slug:slug>/editar/", views.painel_editar, name="painel_editar"),
    path("painel/elevadores/<slug:slug>/excluir/", views.painel_excluir, name="painel_excluir"),
]