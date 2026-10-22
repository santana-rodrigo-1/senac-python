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
    imagem = models.ImageField(upload_to="elevadores/")
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
