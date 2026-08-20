# Exercício 1

nomes = []
qtd  = int(input("Quantidade de Alunos: "))
for i in range(qtd):
    nome = input(f"Nome: {i+1}: ")
    sobrenome = input(f"Sobrenome: {i+1}: ")
    nomes.append(nome)

nomecompleto = (f"{nome} {sobrenome}")


print(f"{nomecompleto}")



