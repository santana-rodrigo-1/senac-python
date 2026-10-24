from django.urls import path
from . import views

urlpatterns = [
    path("elevadores/", views.lista_elevadores, name="catalogo"),
]
