from django.contrib import admin
from .models import Categoria, Elevador


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Elevador)
class ElevadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "estoque", "ativo")
    list_filter = ("categoria", "ativo")
    search_fields = ("nome",)
