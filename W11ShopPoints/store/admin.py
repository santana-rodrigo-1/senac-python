from django.contrib import admin
from .models import Wallpaper


@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "preco",
        "ativo",
        "criado_em",
    )

    list_filter = ("ativo",)

    search_fields = ("nome",)
