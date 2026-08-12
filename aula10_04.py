temperaturas = [[22.5, 31.0, 25.4], 
                [19.0, 26.5, 21.0], 
                [24.0, 33.5, 28.0]]
cidade = ["Cidade A", "Cidade B", "Cidade c"]
horarios = ["Manhã", "Tarde", "Noite"]

print("horario 1", "horario 2", "horario 3")

for i in range(len(temperaturas)):
    print(f"Cidade [i]: ", end= "")

    for j  in range(len(temperaturas[i])):
        print(f"{temperaturas[i][j]} °c", end = "")
print("\n")
print("Temperatura Diagonal")

for i in range(len(temperaturas)):
    print(f"Posição [{i}][{i}] ({cidade[i]} de {horarios[i]}) - {temperaturas[i][i]} ")

print("\n")
print("Maior temperatura")

maior_linha = [max(linha) for linha in temperaturas]
maior_temperatura = max(maior_linha)

print(f"{maior_linha}")
print(f"{maior_temperatura}")
