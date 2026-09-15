"""
Exercício 1 (Estrutura Inicial de Classe)
Crie uma classe Cachorro com os atributos nome e raca.
• Crie o método latir() que exibe: "Au au! Meu nome é [NOME]!".
• Crie o método __str__ para formatar a impressão do objeto.
"""

class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"Au, Au! Meu nome é {self.nome}!")

    def __str__(self):
        return f"Cachorro: {self.nome} (raça: {self.raca})"

meu_dog = Cachorro("Rex", "Labrador")

print()
print("=== DADOS DO CACHORRO ===")

meu_dog.latir()

print(meu_dog)

print("="*25)
print()
