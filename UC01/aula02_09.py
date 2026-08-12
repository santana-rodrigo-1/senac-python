# Holerite (RH)

nome = input ("Digite o nome do funcionário: ")
salario_bruto = float (input(f"Digite o salario_bruto: "))
aliquota_inss = float (input(f"Digite a alíquota do INSS: "))

inss = salario_bruto * aliquota_inss / 100
liquido = salario_bruto - inss
desconto = salario_bruto - liquido

print("\n" + "+" + "-" * 25 + "+" + "\n")
print(f"Holerite: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"INSS {aliquota_inss}%")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Salário Liquido: R$ {liquido:.2f}")
print("\n" + "+" + "-" * 25 + "+" + "\n")
