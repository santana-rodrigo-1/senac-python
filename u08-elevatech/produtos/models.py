from django.db import models


class Elevador(models.Model):
    nome = models.CharField(max_length=120)
    categoria = models.CharField(max_length=60)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to="elevadores/", blank=True)

    def __str__(self):
        # texto que aparece no admin e no shell
        return self.nome
