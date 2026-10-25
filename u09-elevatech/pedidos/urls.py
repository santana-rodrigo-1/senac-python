from django.urls import path
from . import views

urlpatterns = [
    path("carrinho/adicionar/<int:pk>/", views.adicionar, name="carrinho_adicionar"),
    path("carrinho/", views.ver_carrinho, name="ver_carrinho"),
    path("checkout/", views.finalizar, name="finalizar"),
    path("meus-pedidos/", views.meus_pedidos, name="meus_pedidos"),
]
