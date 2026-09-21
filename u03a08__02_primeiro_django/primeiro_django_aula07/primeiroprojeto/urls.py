from django.contrib import admin
from django.urls import path
from u03a08__02_primeiro_django.primeiro_django_aula07.core.views import home, produtos, sobre

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("produtos/", produtos, name="produtos"),
    path("sobre/", sobre, name="sobre"),
]
