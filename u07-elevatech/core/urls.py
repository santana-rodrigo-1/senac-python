from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("cadastro/", views.register, name="register"),
    path("meus-orcamentos/", views.meus_orcamentos, name="meus_orcamentos"),
    path("meu-perfil/", views.editar_perfil, name="editar_perfil"),
    path("termos/", TemplateView.as_view(template_name="core/termos.html"), name="termos"), # <-- ESSA LINHA
    path("contato/", views.contato, name="contato"),
    path("faq/", views.faq, name="faq"),
]