# Frete.
# Calcule o valor do frete considerando uma taxa fixa.
# (preco * preco_kg) + taxa

peso_prod = float(input("\n\nDigite o peso em kg: "))
preco_kg = float(input("Digite o preço do produto por kg: "))
taxa = float(input("Digite o valor da taxa: "))

frete = (peso_prod * preco_kg) + taxa

print(f"\n{"=" * 40}")
print(f"Peso do produto:\t| Kg {peso_prod}")
print(f"Preço do produto:\t| R${preco_kg}")
print(f"Valor da taxa:\t\t| R${taxa}")
print(f"Valor do frete:\t\t| R${frete}")
print(f"\n{"=" * 40}")