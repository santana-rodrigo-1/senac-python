from django.contrib import admin
from django.urls import include, path 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", auth_views.LoginView.as_view()),
    path("logout/", auth_views.LoginView.as_view()),
    path("", include("core.urls")),
    path('produtos/', include("produtos.urls")),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)