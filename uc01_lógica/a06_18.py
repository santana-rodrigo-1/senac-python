# Somando até Zero

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número: "))

    if numero == 0:
        break

    soma += numero
    quantidade += 1

print(f"Quantidade: {quantidade}")
print(f"Soma: {soma}")
