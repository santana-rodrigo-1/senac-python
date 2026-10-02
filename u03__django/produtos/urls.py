from django.urls import path
from . import views

urlpatterns = [
    path("produtos/", views.produtos, name="produtos"),
    path("produtos/esgotados/", views.produtos_esgotados, name="produtos_esgotados"),
    path("produtos/novo/", views.produto_novo, name="produto_novo"),
    path("produtos/<int:id>/", views.produto_detalhe, name="produto_detalhe"),
    path("produtos/<int:id>/editar/", views.produto_editar, name="produto_editar"), # Adicionada a barra no final
    path("produtos/<str:categoria>/", views.produtos_categoria, name="produtos_categoria"), # Fica por último!
]