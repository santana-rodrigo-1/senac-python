# Comissão

venda = float (input(f"Digite o valor da venda: "))
valor_comissao = float (input(f"Digite o porcentagem da comissão: "))
comissao = venda * valor_comissao / 100

print("\n" + "+" + "-" * 25 + "+" + "\n")
print(f"Valor da venda: R$ {venda:.2f}")
print(f"Valor da comissão: R$ {comissao:.2f}")
print("\n" + "+" + "-" * 25 + "+" + "\n")
