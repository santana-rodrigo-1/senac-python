import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from produtos.models import Elevador


class Command(BaseCommand):
    help = "Popula o banco de dados com os elevadores e suas fotos."

    def handle(self, *args, **options):
        self.stdout.write("Limpando banco de dados...")
        Elevador.objects.all().delete()

        self.stdout.write("Criando elevadores e enviando imagens...")

        elevadores = [
            ("ElevaHome 300", "Residencial", 45000.00, 10, "ElevaHome300.png"),
            ("ElevaHome 500", "Residencial", 65000.00, 8, None),
            ("ElevaOffice 800", "Comercial", 95000.00, 5, "ElevaOffice800.png"),
            ("ElevaOffice 1600", "Comercial", 145000.00, 3, None),
            ("ElevaCare 1000", "Hospitalar", 125000.00, 4, "ElevaCare1000.png"),
            ("ElevaCare 1800", "Hospitalar", 185000.00, 2, "ElevaCare1800.png"),
        ]

        for nome, categoria, preco, estoque, arquivo_foto in elevadores:
            elevador = Elevador.objects.create(
                nome=nome, categoria=categoria, preco=preco, estoque=estoque, ativo=True
            )

            if arquivo_foto:
                caminho_foto = os.path.join(
                    settings.BASE_DIR, "fotos_seed", arquivo_foto
                )

                if os.path.exists(caminho_foto):
                    with open(caminho_foto, "rb") as f:
                        elevador.imagem.save(arquivo_foto, File(f), save=True)
                    self.stdout.write(
                        self.style.SUCCESS(f"  [+] Foto de {nome} salva.")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"  [!] Foto {arquivo_foto} não encontrada.")
                    )

        self.stdout.write(self.style.SUCCESS("Sucesso! Banco populado com as imagens."))
