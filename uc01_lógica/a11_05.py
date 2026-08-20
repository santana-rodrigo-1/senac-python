"""
Exercício 3 (Encapsulamento e Validação de Limites)
Crie uma classe Termostato com o atributo temperatura (inicia em 20.0 °C).
• Crie os métodos aumentar(qtd) e diminuir(qtd).
• Regra: Não permita que a temperatura fique abaixo de 0.0 °C nem acima de
40.0 °C.
"""

class Termostato:
    def __init__(self, aumentar, diminuir):
        self.aumentar = aumentar
        self.diminuir = diminuir

