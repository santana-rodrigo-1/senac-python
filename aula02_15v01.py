import subprocess
subprocess.run("cls", shell=True)

nome = input("\n\nDigite nome do funcionário: ")
salario_bruto = float(input("Digite o Salário bruto em R$: "))
vale_transporte = float(input("Digite o valor do vale-transporte em R$: "))

salario_liquido = salario_bruto - vale_transporte

# Definindo uma largura padrão para o bloco (ex: 35 caracteres)
largura_bloco = 35

print(f"\n{'=' * largura_bloco}\n")

# O :<20 alinha o texto à esquerda ocupando exatamente 20 espaços
print(f"Nome:               {nome}")
print(f"Salário Bruto:      R$ {salario_bruto:.2f}")
print(f"Vale-Transporte:    R$ {vale_transporte:.2f}")
print(f"Salário Líquido:    R$ {salario_liquido:.2f}")

print(f"\n{'=' * largura_bloco}\n")
