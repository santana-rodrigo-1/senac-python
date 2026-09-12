class Bolo:
    def __init__(self, sabor, tamanho):
        self.sabor = sabor
        self.tamanho = tamanho

    def mostrar(self):
        print(f"Sabor: {self.sabor}, Tamanho: {self.tamanho}")

bolo1 = Bolo("Chocolate", "Grande")
bolo2 = Bolo("Morango", "Médio")
bolo3 = Bolo("Baunilha", "Pequeno")

bolo1.mostrar()
bolo2.mostrar()
bolo3.mostrar()