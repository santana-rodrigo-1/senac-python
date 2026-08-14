"""
Exercício 4 (Herança e Polimorfismo)
Crie a classe pai Funcionario (nome, salario) com o método calcular_bonus() (10%
do salário).
• Crie a classe filha Gerente que herda de Funcionario e sobrescreve o
método calcular_bonus() para retornar 20% do salário.
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario




calcular_bonus()