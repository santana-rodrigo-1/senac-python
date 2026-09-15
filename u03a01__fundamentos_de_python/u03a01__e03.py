'''
Exercício3 —Sistema de aprovação
'''

nome = input("Digite seu nome: ").capitalize()
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

print(f"Nome: {nome}.")
print(f"suas notas são: {n1:.1f}, {n2:.1f} e {n3:.1f}.")
print(f"Sua média é: {media:.1f}.")

if media >= 7:
    print(f"Situação:Aprovado")
elif media >= 5:
    print(f"Situação:Em recuperação")
else:
    print(f"Situação:Reprovado")