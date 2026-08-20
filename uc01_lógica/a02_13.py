# 2. Crie um programa que solicite dois números ao usuário e exiba o resultado
# da subtração entre eles.
# Exemplo:
# Digite o primeiro número: 20
# Digite o segundo número: 8
# Resultado da subtração: 12

import subprocess
subprocess.run("cls", shell=True)

numero1 = n1 = float(input("\n\nDigite o primeiro número: "))
numero2 = n2 = float(input("Digite o segundo número: "))

subtracao = sub = (n1 - n2)

print(f"\n{n1} - {n2} = {sub}")
print(f"Resultado da subtração: {sub:.1f}.\n\n")

