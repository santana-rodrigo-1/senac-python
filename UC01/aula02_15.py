# 6. Desenvolva um programa que solicite:
# • Nome do funcionário.
# • Salário bruto.
# • Valor do vale-transporte.
# Calcule o salário líquido utilizando a fórmula:
# Salário líquido = Salário bruto - Vale-transporte
# Ao final, exiba um holerite organizado contendo todas as informações.

nome = input("\n\nDigite nome do funcionário: ")
salario_bruto = float(input("Digite o Salário bruto em R$: "))
vale_transporte = float(input("Digite o valor do vale-transporte em R$: "))

salario_liquido = salario_bruto - vale_transporte

print(f"\n{"=" * 30}")
print(f"Nome:\t{nome}")
print(f"Salário Bruto:\t\tR$ {salario_bruto}")
print(f"Vale-Transporte:\tR$ {vale_transporte}")
print(f"Salário Líquido:\tR$ {salario_liquido}")
print(f"{"=" * 30}\n")
