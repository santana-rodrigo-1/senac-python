from django.contrib import admin
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "categoria",
        "preco",
        "ativo",
    )

    list_filter = (
        "categoria",
        "ativo",
    )

    search_fields = (
        "nome",
        "descricao",
    )