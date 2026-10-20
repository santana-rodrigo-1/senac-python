from django.db import models


class Wallpaper(models.Model):

    nome = models.CharField(max_length=150)

    descricao = models.TextField()

    preco = models.PositiveIntegerField()

    imagem = models.ImageField(upload_to="wallpapers/")

    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
