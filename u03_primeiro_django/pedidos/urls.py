from django.urls import path
from . import views

urlpatterns = [
    path("carrinho/", views.ver_carrinho, name="carrinho"),
    path("carrinho/adicionar/<int:id>/", views.adicionar_carrinho, name="adicionar_carrinho"),
    
]