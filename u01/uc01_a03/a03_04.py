# Toco em notas.

valor_compra = int(input("Informe o valor da compra: R$ "))
valor_pago = int(input("Informe o valor pago: R$"))

troco = valor_pago - valor_compra

print(f"Troco: R$ {troco}")

notas100 = troco // 100
troco = troco % 100

notas50 = troco // 50
troco = troco % 50

notas20 = troco // 20
troco = troco % 20

notas10 = troco // 10
troco = troco % 10

notas5 = troco // 5
troco = troco % 5

notas2 = troco // 2
troco = troco % 2

print("Troco em notas")
print(f"Notas de R$100,00: {notas100}")
print(f"Notas de R$50,00: {notas50}")
print(f"Notas de R$20,00: {notas20}")
print(f"Notas de R$10,00: {notas10}")
print(f"Notas de R$5,00: {notas5}")
print(f"Notas de R$2,00: {notas2}")
