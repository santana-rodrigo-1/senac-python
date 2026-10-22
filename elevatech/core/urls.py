from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("cadastro/", views.register, name="register"),
    path("meus-orcamentos/", views.meus_orcamentos, name="meus_orcamentos"),
]