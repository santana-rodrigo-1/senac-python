alunos = ["Gabriel", "Helena", "Igor"]
presencas = [
    [4, 4, 4, 0, 4], # Gabriel faltou quinta
    [4, 4, 4, 4, 4], # helena presença 100%
    [2, 4, 0, 2, 4]  # Igor algumas faltas
]

print("\nFREQUÊNCIA SEMANAL\n")

for i in range(len(alunos)):

    nome_aluno = alunos[i]
    presenca_aluno = presencas[i]
    print(f"Aluno(a): {nome_aluno} - Presença : {presenca_aluno}")

    total_presenca = sum(presencas[i])
    print()
    print(f"Média: {presencas}")

    if total_presenca >= 18:
        print()
        print("FREQUÊNCIA OK.")
    else:
        print()
        print("ALERTA DE FALTAS.")

    maior_nota = min(presencas[i])
    print(f"Menor público total: {min}")

# REQUÊNCIA SEMANAL

