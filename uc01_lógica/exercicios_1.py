print("=" * 40)
print("CADASTRO DE ALUNOS")
print("=" * 40)

quantidade = int(input("Quantos alunos deseja cadastrar? "))

nomes = []
medias = []

for i in range(quantidade):

    print()
    print("Aluno", i + 1)

    nome = input("Nome: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = nota1 + nota2 + nota3 / 3

    nomes.append(nome)
    medias.append(media)

print()
print("=" * 40)
print("RESULTADO")
print("=" * 40)

for i in range(len(nomes)):

    print("Nome:", nomes[i])
    print("Média:", medias[i])

    if medias[i] >= 7:
        print("Aprovado")

    else:
        print("Reprovado")

    print("-" * 30)