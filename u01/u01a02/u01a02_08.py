# IMC (SAÚDE)

peso = float(input(f"Digite o peso: "))
altura = float(input(f"Digite a altura em metros: "))
imc = peso / (altura**2)

print("\n" + "+" + "-" * 25 + "+" + "\n")
print(f"Peso: {peso:.2f}")
print(f"Altura: {altura:.2f}")
print(f"Seu IMC é: {imc:.2f}")
print("\n" + "+" + "-" * 25 + "+" + "\n")
