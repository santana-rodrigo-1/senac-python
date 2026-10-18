# Conversor de moeda

real = float(input(f"Digite o valor em Reais: "))
cotacao = float(input(f"Digite a cotação: "))
cotacao = real / cotacao

print("\n" + "+" + "-" * 25 + "+" + "\n")
print(f"Valor em Real: R$ {real:.2f}")
print(f"Valor em Dólar: US$ {cotacao:.2f}")
print("\n" + "+" + "-" * 25 + "+" + "\n")
