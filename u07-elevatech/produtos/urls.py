from django.urls import path
from . import views

urlpatterns = [
    path("elevadores/", views.lista_elevadores, name="catalogo"),
    # Rotas do Painel
    path("painel/", views.painel, name="painel"),
    path("painel/novo/", views.elevador_novo, name="elevador_novo"),
    path("painel/editar/<int:pk>/", views.elevador_editar, name="elevador_editar"),
    path("painel/excluir/<int:pk>/", views.elevador_excluir, name="elevador_excluir"),
]