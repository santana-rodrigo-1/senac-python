import subprocess
subprocess.run("cls", shell=True)

nome = input("\n\nDigite nome do funcionário: ")
salario_bruto = float(input("Digite o Salário bruto em R$: "))
vale_transporte = float(input("Digite o valor do vale-transporte em R$: "))

salario_liquido = salario_bruto - vale_transporte

# Criamos as linhas de texto primeiro para poder medir o tamanho delas
l1 = f"Nome: {nome}"
l2 = f"Salário Bruto: R$ {salario_bruto:.2f}"
l3 = f"Vale-Transporte: R$ {vale_transporte:.2f}"
l4 = f"Salário Líquido: R$ {salario_liquido:.2f}"

# Descobre qual é a linha mais comprida para o '=' acompanhar
tamanho_da_linha = max(len(l1), len(l2), len(l3), len(l4))

# Exibe o resultado perfeitamente alinhado
print(f"\n{'=' * tamanho_da_linha}\n")
print(l1)
print(l2)
print(l3)
print(l4)
print(f"\n{'=' * tamanho_da_linha}\n")
