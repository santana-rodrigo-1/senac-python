from django.shortcuts import render

from .models import Wallpaper


def home(request):

    wallpapers = Wallpaper.objects.filter(ativo=True)

    return render(request, "store/home.html", {"wallpapers": wallpapers})
