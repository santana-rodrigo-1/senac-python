from django.urls import path
from .views import home, escadas

urlpatterns = [
    path("", home, name="home"),
    path("escadas/", escadas, name="escadas"),
]
