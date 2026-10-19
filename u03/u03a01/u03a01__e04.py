"""
Exercício4 —Processo seletivo JWCA JWC recebeu um candidato
O programa deverá solicitar:

Regras:
O candidato passa para a próxima etapa se:
•tiver 18 anos ou mais;
•tiver experiência;
•nota do teste for maior ou igual a 7.
"""

print()
q1 = input("Digite nome: ").capitalize()
q2 = int(input("Digite idade: "))
q3 = input("Experiência em programação: (sim/não)").strip().lower()
q4 = int(input("Confirme sua nota no texte: "))

print()
print(f"Nome: {q1}!")
print(f"Idade: {q2} anos.")
print(f"Experiência {q3}.")
print(f"Sua nota é {q4}.")
if q4 >= 7 and q3 == "sim":
    print(f"Situação:Aprovado")
elif q4 >= 5 and q3 == "sim":
    print(f"Situação:Recuperação")
else:
    print(f"Situação:Reprovado")
print()
