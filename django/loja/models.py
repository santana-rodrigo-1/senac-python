from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200,null=True,blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

def __self__(self):
    return self.nome