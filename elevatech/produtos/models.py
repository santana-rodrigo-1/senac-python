from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(unique=True)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Elevador(models.Model):
    class Tipo(models.TextChoices):
        RESIDENCIAL = "residencial", "Residencial"
        COMERCIAL = "comercial", "Comercial"
        HOSPITALAR = "hospitalar", "Hospitalar"

    nome = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="elevadores"
    )
    descricao_curta = models.CharField(max_length=200)
    descricao = models.TextField()
    capacidade_kg = models.PositiveIntegerField(help_text="Carga máxima em kg")
    velocidade = models.DecimalField(
        max_digits=4, decimal_places=2, help_text="Velocidade em m/s"
    )
    pavimentos = models.PositiveIntegerField(help_text="Nº máximo de paradas")
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        help_text="Preço de venda em R$",
    )
    imagem = models.ImageField(upload_to="elevadores/", blank=True, null=True)
    imagem_secundaria = models.ImageField(
        upload_to="elevadores/", blank=True, null=True
    )
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-destaque", "nome"]
        verbose_name_plural = "Elevadores"

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

    def get_absolute_url(self):
        return reverse("produto_detalhe", kwargs={"slug": self.slug})


class SolicitacaoOrcamento(models.Model):
    class Status(models.TextChoices):
        NOVO = "novo", "Novo"
        EM_ANALISE = "analise", "Em análise"
        RESPONDIDO = "respondido", "Respondido"
        FECHADO = "fechado", "Fechado"

    elevador = models.ForeignKey(
        Elevador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="solicitacoes",
        help_text="Deixe em branco para orçamento geral",
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orcamentos",
        help_text="Preenchido automaticamente quando o cliente está logado.",
    )
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    pavimentos = models.PositiveIntegerField(help_text="Nº de andares do prédio")
    mensagem = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.NOVO
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "Solicitação de orçamento"
        verbose_name_plural = "Solicitações de orçamento"

    def __str__(self):
        alvo = self.elevador.nome if self.elevador else "Orçamento geral"
        return f"{self.nome} — {alvo}"


class Pedido(models.Model):
    class Status(models.TextChoices):
        NOVO = "novo", "Novo"
        PAGO = "pago", "Pago"
        ENVIADO = "enviado", "Enviado"
        ENTREGUE = "entregue", "Entregue"
        CANCELADO = "cancelado", "Cancelado"

    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pedidos"
    )
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField(help_text="Endereço completo de entrega")
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.NOVO
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido #{self.pk} — {self.nome}"

    @property
    def total(self):
        return sum(item.subtotal for item in self.itens.all())

    @property
    def total_itens(self):
        return sum(item.quantidade for item in self.itens.all())


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, related_name="itens", on_delete=models.CASCADE
    )
    elevador = models.ForeignKey(Elevador, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Item do pedido"
        verbose_name_plural = "Itens do pedido"

    def __str__(self):
        return f"{self.quantidade}x {self.elevador.nome}"

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario