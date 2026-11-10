from django.urls import path
from . import views

urlpatterns = [
    path("elevadores/", views.lista_elevadores, name="catalogo"),
    path("elevadores/novo/", views.elevador_novo, name="elevador_novo"),
    path("elevadores/<int:pk>/editar/", views.elevador_editar, name="elevador_editar"),
    path("elevadores/<int:pk>/", views.detalhe_elevador, name="elevador_detalhe"),
]
