print("=" * 50)
print("PESQUISA")
print("=" * 50)

quantidade = int(input("Quantidade de pessoas: "))

nomes = []
idades = []

for i in range(quantidade):

    print()

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    nomes.append(nome)
    idades.append(idade)

maior = 0
nome_maior = ""

menor = 200
nome_menor = ""

for i in range(len(idades)):

    if idades[i] > maior:
        maior = idades[i]

    nome_maior = nomes[i]

    if idades[i] < menor:
        menor = idades[i]
        nome_menor = nomes[i]

print()
print("=" * 50)

print("Pessoa mais velha")
print(nome_maior)
print(maior)

print()

print("Pessoa mais nova")
print(nome_menor)
print(menor)