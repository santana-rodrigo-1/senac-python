from django.urls import path
from .views import *  # usar (*) asteristico no lugar de: home, produtos, etc.

urlpatterns = [
    path("", home, name="home"),
    path("produtos/", produtos, name="produtos"),
]
