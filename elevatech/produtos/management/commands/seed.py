from django.core.management.base import BaseCommand
from django.utils.text import slugify

from produtos.models import Categoria, Elevador

CATEGORIAS = [
    {
        "nome": "Linha Compacto",
        "descricao": "Elevadores de pequeno porte para espaços reduzidos.",
    },
    {
        "nome": "Linha Padrão",
        "descricao": "Modelos versáteis para uso residencial, comercial e hospitalar.",
    },
    {
        "nome": "Linha Premium",
        "descricao": "Alto desempenho, acabamento refinado e tecnologia embarcada.",
    },
    {
        "nome": "Linha Alta Capacidade",
        "descricao": "Projetados para grandes fluxos: shoppings, hospitais e edifícios corporativos.",
    },
]


ELEVADORES = [
    {
        "nome": "ElevaHome 300",
        "tipo": "residencial",
        "categoria": "Linha Compacto",
        "descricao_curta": "Compacto para residências de até 3 pavimentos.",
        "descricao": (
            "O ElevaHome 300 foi projetado para casas e sobrados que precisam "
            "de mobilidade vertical sem ocupar muito espaço. Motor silencioso, "
            "cabine reduzida e instalação simplificada. Ideal para reformas em "
            "imóveis já habitados, com prazo de instalação de até 15 dias."
        ),
        "capacidade_kg": 300,
        "velocidade": "0.63",
        "pavimentos": 3,
        "destaque": True,
    },
    {
        "nome": "ElevaHome 500",
        "tipo": "residencial",
        "categoria": "Linha Padrão",
        "descricao_curta": "Conforto e silêncio para condomínios residenciais.",
        "descricao": (
            "Com capacidade para 6 passageiros, o ElevaHome 500 é a escolha "
            "mais comum para prédios residenciais de médio porte. Cabine "
            "acabada em inox escovado, iluminação em LED e portas automáticas "
            "com sensor de presença. Consumo energético otimizado."
        ),
        "capacidade_kg": 500,
        "velocidade": "1.00",
        "pavimentos": 8,
        "destaque": False,
    },
    {
        "nome": "ElevaOffice 800",
        "tipo": "comercial",
        "categoria": "Linha Padrão",
        "descricao_curta": "Alta frequência de uso para escritórios e clínicas.",
        "descricao": (
            "Pensado para edifícios comerciais com fluxo intenso, o ElevaOffice "
            "800 entrega 10 passageiros por viagem, com portas de abertura "
            "central e sistema de tráfego inteligente que reduz o tempo de espera. "
            "Acabamento em aço inoxidável e piso em granito antiderrapante."
        ),
        "capacidade_kg": 800,
        "velocidade": "1.75",
        "pavimentos": 15,
        "destaque": True,
    },
    {
        "nome": "ElevaOffice 1600",
        "tipo": "comercial",
        "categoria": "Linha Premium",
        "descricao_curta": "Alta performance para edifícios corporativos.",
        "descricao": (
            "Para torres corporativas e centros empresariais, o ElevaOffice 1600 "
            "oferece velocidade de 2,5 m/s, sistema de regeneração de energia "
            "(devolve à rede parte do que consome) e cabine com painel touch. "
            "Compatível com integração a sistemas de controle de acesso do prédio."
        ),
        "capacidade_kg": 1600,
        "velocidade": "2.50",
        "pavimentos": 25,
        "destaque": False,
    },
    {
        "nome": "ElevaCare 1000",
        "tipo": "hospitalar",
        "categoria": "Linha Padrão",
        "descricao_curta": "Conforto e acessibilidade para clínicas e hospitais.",
        "descricao": (
            "Projetado para ambientes de saúde, o ElevaCare 1000 atende às "
            "normas ABNT NBR 16000 com cabine ampla, corrimão contínuo, botoeira "
            "em braille e sistema de chamada prioritária. Aceita macas e cadeiras "
            "de rodas com folga. Pintura antimicrobiana nas superfícies de contato."
        ),
        "capacidade_kg": 1000,
        "velocidade": "1.00",
        "pavimentos": 12,
        "destaque": True,
    },
    {
        "nome": "ElevaCare 1800",
        "tipo": "hospitalar",
        "categoria": "Linha Alta Capacidade",
        "descricao_curta": "Para grandes hospitais e centros cirúrgicos.",
        "descricao": (
            "O ElevaCare 1800 é o nosso modelo hospitalar de maior porte: "
            "cabine que acomoda cama hospitalar, equipe médica e equipamentos "
            "simultaneamente. Sistema de emergência com bateria para 30 minutos, "
            "portas com abertura lateral dupla e ventilação forçada. "
            "Manutenção preventiva inclusa no primeiro ano."
        ),
        "capacidade_kg": 1800,
        "velocidade": "1.50",
        "pavimentos": 18,
        "destaque": False,
    },
]


class Command(BaseCommand):
    help = "Popula o banco com categorias e elevadores de exemplo."

    def add_arguments(self, parser):
        parser.add_argument(
            "--limpar",
            action="store_true",
            help="Remove elevadores e categorias existentes antes de semear.",
        )

    def handle(self, *args, **options):
        if options["limpar"]:
            total_el = Elevador.objects.count()
            total_cat = Categoria.objects.count()
            Elevador.objects.all().delete()
            Categoria.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(
                    f"Limpou {total_el} elevador(es) e {total_cat} categoria(s)."
                )
            )

        # --- categorias ---
        self.stdout.write(self.style.MIGRATE_HEADING("\nCategorias:"))
        cat_map = {}
        for item in CATEGORIAS:
            slug = slugify(item["nome"])
            obj, criado = Categoria.objects.get_or_create(
                slug=slug,
                defaults={"nome": item["nome"], "descricao": item["descricao"]},
            )
            cat_map[item["nome"]] = obj
            marca = "+" if criado else "="
            estilo = self.style.SUCCESS if criado else self.style.WARNING
            self.stdout.write(estilo(f"  {marca} {obj.nome}"))

        # --- elevadores ---
        self.stdout.write(self.style.MIGRATE_HEADING("\nElevadores:"))
        criados = 0
        for item in ELEVADORES:
            slug = slugify(item["nome"])
            obj, criado = Elevador.objects.get_or_create(
                slug=slug,
                defaults={
                    "nome": item["nome"],
                    "tipo": item["tipo"],
                    "categoria": cat_map[item["categoria"]],
                    "descricao_curta": item["descricao_curta"],
                    "descricao": item["descricao"],
                    "capacidade_kg": item["capacidade_kg"],
                    "velocidade": item["velocidade"],
                    "pavimentos": item["pavimentos"],
                    "destaque": item["destaque"],
                    "ativo": True,
                },
            )
            if criado:
                criados += 1
            marca = "+" if criado else "="
            estilo = self.style.SUCCESS if criado else self.style.WARNING
            self.stdout.write(
                estilo(f"  {marca} {obj.nome} ({obj.get_tipo_display()})")
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nPronto! {criados} elevador(es) novo(s) criado(s). "
                f"Total no banco: {Elevador.objects.count()} elevadores, "
                f"{Categoria.objects.count()} categorias."
            )
        )
        self.stdout.write(
            "Acesse /admin/ para subir imagens, ou /elevadores/ para ver o catálogo."
        )
