print("==============================")
print("      ELEIÇÃO DA TURMA")
print("==============================")

candidatos = [
    {"numero": 1, "nome": "Ana", "votos": 0},
    {"numero": 2, "nome": "Bruno", "votos": 0},
    {"numero": 3, "nome": "Carlos", "votos": 0}
]

nulos = 0

quantidade_eleitores = int(input("Quantidade de eleitores: "))

for i in range(quantidade_eleitores):

    print()
    print("Eleitor", i + 1)

    print("1 - Ana")
    print("2 - Bruno")
    print("3 - Carlos")
    print("0 - Voto nulo")

    voto = int(input("Digite seu voto: "))

    if voto == 1:
        candidatos[0]["votos"] += 1

    elif voto == 2:
        candidatos[1]["votos"] += 1

    elif voto == 3:
        candidatos[2]["votos"] += 1

    elif voto == 0:
        nulos += 1

    else:
        print("Voto inválido! Digite novamente.")

        # Repetir o voto inválido
        while voto not in [0, 1, 2, 3]:
            voto = int(input("Digite seu voto novamente: "))

        if voto == 1:
            candidatos[0]["votos"] += 1

        elif voto == 2:
            candidatos[1]["votos"] += 1

        elif voto == 3:
            candidatos[2]["votos"] += 1

        elif voto == 0:
            nulos += 1


# Resultado
print()
print("==============================")
print("        RESULTADO")
print("==============================")

for candidato in candidatos:
    print(candidato["nome"], "-", candidato["votos"], "votos")

print("Nulos -", nulos, "votos")


# Identificar maior quantidade de votos
maior_votos = candidatos[0]["votos"]

for candidato in candidatos:

    if candidato["votos"] > maior_votos:
        maior_votos = candidato["votos"]


# Verificar empate
quantidade_maiores = 0

for candidato in candidatos:

    if candidato["votos"] == maior_votos:
        quantidade_maiores += 1


if quantidade_maiores > 1:

    print()
    print("==============================")
    print("          EMPATE!")
    print("==============================")

    for candidato in candidatos:

        if candidato["votos"] == maior_votos:
            print(candidato["nome"], ":", candidato["votos"], "votos")

else:

    for candidato in candidatos:

        if candidato["votos"] == maior_votos:
            print()
            print("==============================")
            print("VENCEDOR:", candidato["nome"])
            print("==============================")
            print("Total de votos:", candidato["votos"])


# Bônus
votos_validos = quantidade_eleitores - nulos

print()
print("Total de votos válidos:", votos_validos)
print("Total de votos nulos:", nulos)

if votos_validos > 0:
    percentual = (maior_votos / votos_validos) * 100
    print(f"Percentual de votos da vencedora: {percentual:.2f}%")