# 5. Solicite o valor da conta de um restaurante.
# O programa deve calcular:
# • 10% de gorjeta.
# • Valor total a ser pago.
# Exiba os dois valores formatados com duas casas decimais.

conta = float(input(f"\n\nDigite o valor da conta em R$: "))

gorjeta = conta * 0.10
total = conta + gorjeta

print(f"\nConta:\t\tR$ {conta:.2f}\t.")
print(f"Gorjeta (10%):\tR$ {gorjeta:.2f}\t.")
print(f"Total a pagar:\tR$ {total:.2f}\t.\n\n")
