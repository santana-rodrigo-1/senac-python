# 5 — Aprovado ou reprovado
# Peça duas notas de um aluno e calcule a média entre elas.
# Se a média for menor que 6, exiba "Reprovado". Caso
# contrário, exiba "Aprovado".

v01 = float(input("\nDigite a nota 01: "))
v02 = float(input("Digite a nota 02: "))

media = (v01 + v02) / 2

print(f"\nNota 01: {v01} + Nota 02: {v02}")
print(f"Sua média é: {media}")
if media < 6:
    print("\nREPROVADO\n")
else:
    print("\nAPROVADO\n")
