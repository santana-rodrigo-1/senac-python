"""
Exercício 2 (Métodos e Mudança de Estado)
Crie uma classe Lampada com o atributo ligada (que começa como False).
• Crie os métodos ligar(), desligar() e status().
"""

class Lampada:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print("A lampada foi LIGADA.")

    def desligar(self):
        self.ligada = False
        print("A lampada doi DESLIGADA.")

    def status(self):
        if self.ligada:
            print("STATUS: Lampada ACESA")
        else:
            print("STATUS: Lampada APAGADA")

lampada = Lampada()
lampada.status()
lampada.ligar()
lampada.status()
lampada.desligar()
