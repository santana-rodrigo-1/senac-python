# Maior número

maior = int(input("Informe o 1° número: "))

for i in range(2, 6):
    num = int(input(f"Informe o {i}° número: "))
    if num > maior:
        maior = num
    

print(f"O Maior número é: {maior}")
