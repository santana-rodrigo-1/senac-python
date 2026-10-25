from django.core.management.base import BaseCommand
from produtos.models import Categoria, Elevador

class Command(BaseCommand):
    help = 'Popula o banco com os elevadores da ElevaTech'

    def handle(self, *args, **options):
        self.stdout.write("Limpando dados antigos...")
        Elevador.objects.all().delete()
        Categoria.objects.all().delete()

        self.stdout.write("Criando categorias...")
        cat_res = Categoria.objects.create(nome="Linha Residencial")
        cat_com = Categoria.objects.create(nome="Linha Comercial")
        cat_hos = Categoria.objects.create(nome="Linha Hospitalar")

        self.stdout.write("Criando elevadores...")
        
        elevadores = [
            # (nome, categoria, preco, estoque)
            ("ElevaHome 300", cat_res, 45000.00, 10),
            ("ElevaHome 500", cat_res, 65000.00, 8),
            ("ElevaOffice 800", cat_com, 95000.00, 5),
            ("ElevaOffice 1600", cat_com, 145000.00, 3),
            ("ElevaCare 1000", cat_hos, 125000.00, 4),
            ("ElevaCare 1800", cat_hos, 185000.00, 2),
        ]

        for nome, cat, preco, estoque in elevadores:
            Elevador.objects.create(
                nome=nome, 
                categoria=cat, 
                preco=preco, 
                estoque=estoque, 
                ativo=True
            )

        self.stdout.write(self.style.SUCCESS("Sucesso! Elevadores criados."))