from django.urls import path
from . import views

urlpatterns = [
    path('painel/', views.painel_home, name='painel_home'),
    path('painel/produtos/', views.painel_produtos, name='painel_produtos'),
    path('painel/pedidos/', views.painel_pedidos, name='painel_pedidos'),
]