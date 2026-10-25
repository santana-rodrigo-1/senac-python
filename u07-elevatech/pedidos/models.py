from django.db import models
from django.contrib.auth.models import User
from produtos.models import Elevador

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="novo")

    def __str__(self):
        return f"Pedido #{self.pk} - {self.usuario.username}"

    @property
    def total(self):
        return sum(item.subtotal for item in self.itens.all())

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name="itens", on_delete=models.CASCADE)
    elevador = models.ForeignKey(Elevador, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantidade * self.preco