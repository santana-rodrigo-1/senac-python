from django.urls import path
from . import views

urlpatterns = [
    path("elevadores/", views.catalogo, name="catalogo"),
    path("elevadores/<slug:slug>/", views.detalhe, name="produto_detalhe"),
    path("orcamento/", views.orcamento, name="orcamento"),
]
