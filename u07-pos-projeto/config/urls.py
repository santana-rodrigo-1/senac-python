from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# --- PERSONALIZAÇÃO DO ADMIN ---
admin.site.site_header = "ElevaTech | Administração"
admin.site.site_title = "ElevaTech"
admin.site.index_title = "Gestão do Sistema"
# -------------------------------

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('dashboard.urls')),
    path("contas/", include("django.contrib.auth.urls")),
    path("", include("core.urls")),
    path("", include("produtos.urls")),
    path("", include("pedidos.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
