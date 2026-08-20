# 6 — O maior de três números
# Peça três números diferentes ao usuário e exiba qual deles é o maior.
# Dica: Você vai precisar combinar mais de uma condição.
# Pense em comparar o primeiro número com os outros dois,
# usando if, elif e else.

v01 = float(input("\nDigite um 1° número: "))
v02 = float(input("Digite um 2° número: "))
v03 = float(input("Digite um 3° número: "))

if v01 > v02:
    print(f"\nO maior número é: {v01} .\n")
elif v02 > v03:
    print(f"\nO maior número é: {v02} .\n")
else:
    print(f"\nO maior número é: {v03} .\n")
 