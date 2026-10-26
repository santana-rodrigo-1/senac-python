from django.contrib import admin
from django.utils.html import format_html

from .models import Categoria, Elevador, SolicitacaoOrcamento, Pedido, ItemPedido


# =============================================================
# Branding global do admin (aparece no topo e no título da aba)
# =============================================================
admin.site.site_header = "ElevaTech — Administração"
admin.site.site_title = "ElevaTech Admin"
admin.site.index_title = "Painel de Controle"


# =============================================================
# Categoria
# =============================================================
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "slug", "total_elevadores")
    search_fields = ("nome", "slug")
    prepopulated_fields = {"slug": ("nome",)}

    @admin.display(description="Elevadores")
    def total_elevadores(self, obj):
        return obj.elevadores.count()


# =============================================================
# Elevador
# =============================================================
@admin.register(Elevador)
class ElevadorAdmin(admin.ModelAdmin):
    list_display = (
        "nome", "tipo_badge", "categoria", "capacidade_kg",
        "velocidade", "preco", "destaque_badge", "ativo_badge", "criado_em",
    )
    list_filter = ("tipo", "categoria", "destaque", "ativo")
    search_fields = ("nome", "slug", "descricao_curta", "descricao")
    prepopulated_fields = {"slug": ("nome",)}
    readonly_fields = ("criado_em",)
    list_per_page = 20
    date_hierarchy = "criado_em"
    fieldsets = (
        ("Identificação", {
            "fields": ("nome", "slug", "tipo", "categoria")
        }),
        ("Descrição", {
            "fields": ("descricao_curta", "descricao")
        }),
        ("Especificações técnicas", {
            "fields": ("capacidade_kg", "velocidade", "pavimentos", "preco")
        }),
        ("Imagens", {
            "fields": ("imagem", "imagem_secundaria")
        }),
        ("Visibilidade", {
            "fields": ("destaque", "ativo", "criado_em")
        }),
    )

    @admin.display(description="Tipo", ordering="tipo")
    def tipo_badge(self, obj):
        cores = {
            "residencial": "#3498db",
            "comercial": "#9b59b6",
            "hospitalar": "#2ecc71",
        }
        cor = cores.get(obj.tipo, "#95a5a6")
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 9px;'
            'border-radius:10px;font-size:11px;font-weight:600;">{}</span>',
            cor, obj.get_tipo_display(),
        )

    @admin.display(description="Destaque", boolean=True)
    def destaque_badge(self, obj):
        return obj.destaque

    @admin.display(description="Ativo", boolean=True)
    def ativo_badge(self, obj):
        return obj.ativo


# =============================================================
# Solicitação de orçamento
# =============================================================
@admin.register(SolicitacaoOrcamento)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = (
        "id_link", "nome", "elevador", "telefone",
        "cidade", "status_badge", "criado_em",
    )
    list_filter = ("status", "elevador__tipo", "criado_em")
    search_fields = ("nome", "email", "telefone", "cidade")
    readonly_fields = ("criado_em", "usuario")
    list_per_page = 25
    date_hierarchy = "criado_em"
    list_select_related = ("elevador", "usuario")
    fieldsets = (
        ("Solicitante", {
            "fields": ("nome", "email", "telefone", "cidade", "usuario")
        }),
        ("Sobre o projeto", {
            "fields": ("elevador", "pavimentos", "mensagem")
        }),
        ("Atendimento", {
            "fields": ("status", "criado_em")
        }),
    )

    @admin.display(description="#", ordering="id")
    def id_link(self, obj):
        return format_html("<strong>#{}</strong>", obj.pk)

    @admin.display(description="Status", ordering="status")
    def status_badge(self, obj):
        cores = {
            "novo": "#ff6b35",
            "analise": "#3498db",
            "respondido": "#2ecc71",
            "fechado": "#95a5a6",
        }
        cor = cores.get(obj.status, "#95a5a6")
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 9px;'
            'border-radius:10px;font-size:11px;font-weight:600;">{}</span>',
            cor, obj.get_status_display(),
        )


# =============================================================
# Pedidos (Carrinho)
# =============================================================
class ItemInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ("elevador", "quantidade", "preco_unitario")
    can_delete = False


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "usuario", "status", "total_exibido", "criado_em")
    list_filter = ("status", "criado_em")
    search_fields = ("nome", "email", "telefone")
    readonly_fields = ("usuario", "criado_em")
    inlines = [ItemInline]
    date_hierarchy = "criado_em"
    list_per_page = 25

    @admin.display(description="Total")
    def total_exibido(self, obj):
        return f"R$ {obj.total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")