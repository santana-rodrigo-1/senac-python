from django.contrib import admin
from .models import Categoria, Elevador, SolicitacaoOrcamento


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "slug")
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Elevador)
class ElevadorAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "tipo",
        "capacidade_kg",
        "velocidade",
        "destaque",
        "ativo",
    )
    list_filter = ("tipo", "categoria", "destaque", "ativo")
    search_fields = ("nome", "descricao_curta")
    prepopulated_fields = {"slug": ("nome",)}
    list_editable = ("destaque", "ativo")


@admin.register(SolicitacaoOrcamento)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "elevador", "telefone", "status", "criado_em")
    list_filter = ("status", "elevador__tipo")
    search_fields = ("nome", "email", "telefone")
    readonly_fields = ("criado_em",)
