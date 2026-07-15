# 1 — Quatro operações
# Peça ao usuário dois números e mostre na tela o resultado da soma, subtração, multiplicação e divisão
# entre eles.
# Dica: Use input() para receber os valores e float() para transformar o texto digitado em número.

num1 = float(input("\nDigite um número: "))
num2 = float(input("Digite outro número: "))

soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
divi = num1 / num2

LARGURA = 50

print(f"{'=' * LARGURA}\n")

print(f"Os números digitados são: {num1} e {num2}")
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subt}")
print(f"Multiplicação: {num1} x {num2} = {mult}")
print(f"Divisão: {num1} / {num2} = {divi}")

print(f"{'=' * LARGURA}\n")
