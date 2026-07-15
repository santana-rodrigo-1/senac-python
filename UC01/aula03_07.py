# Investimento
# Calcule os juros simples e o valor total da aplicação.
# capital + (capital * taxa * meses)

capital_inic = float(input("\n\nDigite seu capital inicial: "))
taxa = float(input("Digite a taxa: "))
meses = float(input("Digite o total de meses investido: "))

capital_fim = capital_inic + (capital_inic * taxa * meses)

print(f"\n{"=" * 40}")
print(f"{'INVESTIMENTO SENAC':^40}")
print(f"{"=" * 40}")
print(f"Capital inicial é:\t| R$ {capital_inic:.2f}")
print(f"Taxa aplicada foi de :\t| {taxa} %")
print(f"Meses aplicados foi:\t| mês(es){meses}")
print(f"Capital final é:\t| R$ {capital_fim:.2f}")
print(f"{"=" * 40}\n\n")
