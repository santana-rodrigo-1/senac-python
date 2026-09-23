from django.urls import path
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("produtos/", produtos, name="produtos"),
    path("sobre/", sobre, name="sobre"),
]