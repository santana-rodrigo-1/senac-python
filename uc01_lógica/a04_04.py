# 4 — Par ou ímpar
# Peça um número inteiro e informe se ele é par ou ímpar.
# Dica: Um número é par quando o resto da divisão por 2 é igual a zero.
# Em Python, o resto da divisão se calcula com o
# operador % (exemplo: numero % 2).

v01 = int(input("\nDigite um número inteiro: "))

v02 = v01 % 2

if v02 == 0:
    print("O número é: PAR.")
else:
    print("O número é: ÍMPAR.")
