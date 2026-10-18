# Calculadora de troco - Varejo

total = float(input("Digite o Valor da Compra: "))
pago = float(input("Digite o Valor Pago: "))
troco = pago - total

print("\n" + "+" + "-" * 25 + "+")
print(f"o valor do troco é: {troco:.2f}")
print("+" + "-" * 25 + "+" + "\n")
