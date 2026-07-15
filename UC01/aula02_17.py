# 8. Recibo de Supermercado
# Desenvolva um programa que solicite:
# • Nome do cliente.
# • Nome do produto.
# • Preço unitário.
# • Quantidade comprada.
# • Valor pago.
# O programa deverá calcular:
# • Subtotal (preço × quantidade).
# • Troco.
# • Ao final, exiba um recibo organizado contendo todas essas informações.

nome_cliente = input("\n\nDigite seu nome: ").strip().upper()
nome_produto = input("Digite nome do produto: ").strip().upper()
valor_unit = float(input("Digite valor unitario do produto: "))
quant_produto = float(input("Digite a quantidade comprada:"))
valor_pago = float(input("Digite o valor pago em R$: "))

subtotal = valor_unit * quant_produto
troco = valor_pago - subtotal

print(f"\n{"=" * 40}")
print(f"{'RECIBO SUPERMERCADO SENAC':^40}")
print(f"{"=" * 40}")
print(f"Nome:\t\t- {nome_cliente}")
print(f"Produto:\t- {nome_produto}")
print(f"Preço unitário:\t- R$ {valor_unit:.2f}")
print(f"Quantidade:\t- UN {quant_produto:.0f}")
print(f"Valor pago:\t- R$ {valor_pago:.2f}")
print(f"Subtotal:\t- R$ {subtotal:.2f}")
print(f"Troco:\t\t- R$ {troco:.2f}")
print(f"{"=" * 40}\n\n")
