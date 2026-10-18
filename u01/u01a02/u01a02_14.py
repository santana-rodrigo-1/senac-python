# 3. Solicite um número ao usuário e mostre:
# • O dobro do número.
# • O triplo do número.

# import subprocess
# subprocess.run("cls", shell=True)

numero = float(input("\n\nDigite um número: "))
dobro = numero * 2
triplo = numero * 3

print(f"\nO número digitado é: {numero}")
print(f"O dobro  de {numero} é: {dobro}.")
print(f"O triplo de {numero} é: {triplo}.\n\n")
