import subprocess
subprocess.run("cls", shell=True)

nome = input("\n\nDigite nome do funcionário: ")
salario_bruto = float(input("Digite o Salário bruto em R$: "))
vale_transporte = float(input("Digite o valor do vale-transporte em R$: "))

salario_liquido = salario_bruto - vale_transporte

# Definimos uma largura fixa de 20 espaços apenas para os textos da esquerda
largura_texto = 20

l1 = f"{'Nome:'.ljust(largura_texto)}{nome}"
l2 = f"{'Salário Bruto:'.ljust(largura_texto)}R$ {salario_bruto:.2f}"
l3 = f"{'Vale-Transporte:'.ljust(largura_texto)}R$ {vale_transporte:.2f}"
l4 = f"{'Salário Líquido:'.ljust(largura_texto)}R$ {salario_liquido:.2f}"

# O '=' continua automático, medindo a linha mais comprida
tamanho_da_linha = max(len(l1), len(l2), len(l3), len(l4))

print(f"\n{'=' * tamanho_da_linha}\n")
print(l1)
print(l2)
print(l3)
print(l4)
print(f"\n{'=' * tamanho_da_linha}\n")
