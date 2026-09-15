'''
Exercício1 —Aquecimento
"Cadastro do candidato JWC"
Crie um programa que pergunte:
•Nome
•Idade
•Cidade
•Linguagem de programação favorita
'''

print()

q1 = input("Digite seu nome: ").capitalize()
q2 = int(input("Digite sua idade: "))
q3 = input("Digite sua cidade: ").capitalize()
q4 = input("Digite sua linguagem de programação favorita: ").capitalize()

print()
print(f"Olá, {q1}!")
print(f"Você tem {q2} anos.")
print(f"Mora em {q3}.")
print(f"Sua linguagem favorita é {q4}.")
print()