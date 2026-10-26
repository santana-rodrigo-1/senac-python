from django.db import models

class Elevador(models.Model):
    nome = models.CharField(max_length=120)
    categoria = models.CharField(max_length=60)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to="elevadores/", blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Elevadores"