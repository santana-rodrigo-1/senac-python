from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"


@receiver(post_save, sender=User)
def gerenciar_perfil(sender, instance, created, **kwargs):
    if created:
        # Se o usuário é novo, cria o perfil
        Perfil.objects.create(usuario=instance)
    else:
        # Se o usuário já existe (ex: admin01), garante que o perfil exista
        # O get_or_create busca o perfil. Se não achar, ele cria um vazio na hora!
        Perfil.objects.get_or_create(usuario=instance)