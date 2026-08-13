alunos = ["Ana", "Bruno", "Carla", "Diego"]
notas = [[7.5, 8.0, 9.0],
         [5.0, 6.0, 4.5],
         [9.0, 9.5, 10.0],
         [6.5, 7.0, 7.0],
         ]

print("Boletim da turma")

for i in range(len(alunos)):

    nome = alunos[i]
    nota_aluno = notas[i]
    print(f"Aluno(a): {nome} - Notas: {nota_aluno}")

    media = sum(nota_aluno)/len(nota_aluno)
    print(f"Média: {media}")

    if media >= 7.0:
        print("APROVADO.")
    else:
        print("REPROVADO.")

    maior_nota = max(nota_aluno)
    print(f"Maior nota: {max}")
    print("\n")
    print("-" * 15)


