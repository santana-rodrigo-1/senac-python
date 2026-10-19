"""
Exercício2 —Calculadora JWC
Solicite dois números.
"""

print()
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
div = n1 / n2
divint = n1 // n2
resto = n1 % n2
potencia = n1**n2

print()
print(f"Soma: {soma}.")
print(f"Subtração: {subtracao}.")
print(f"Divisão: {div}.")
print(f"Divisão inteira: {divint}.")
print(f"Resto da divisão: {resto}.")
print(f"Potenciação: {potencia}.")
print()
