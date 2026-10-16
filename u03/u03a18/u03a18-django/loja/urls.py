from django.urls import path
from .views import home # ou from . import views.home

urlpatterns = [
    path('', home, name="home"),
]
