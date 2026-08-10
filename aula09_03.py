notas = []
qtd  = int(input("Quantos alunos? "))
for i in range(qtd):
    nota = float(input(f"Aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média: {media:.1f}")
print(f"Maior: {max(notas)}")
print(f"Menor: {min(notas)}")
