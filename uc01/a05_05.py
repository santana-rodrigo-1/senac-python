# Bolsa de estudos (or)
# O aluno poderá receber a bolsa se possuir média alta
# ou baixa renda familiar
# media >= 9 or renda_familiar <= 2000

media = float(input("\nDigite a média: "))
renda_familiar = float(input("Digite a renda em R$: "))

if media >= 9 or renda_familiar <= 2000:
    print("\nBolsa aprovada.\n")
else:
    print("\nBolsa negada.\n")
