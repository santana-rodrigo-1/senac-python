# 2.
def obter_dobro_dos_pares(lista):
    resultado = []

    for valor in lista:
        if valor % 2 == 0:
            dobro = valor * 2
            resultado.append(valor)
        return resultado

numeros = [12, 5, 8, 21 , 30, 4 ,15, 2]

ultimos_3 = numeros[-3:]
dobro_dos_pares = obter_dobro_dos_pares(numeros)

print("3 úçtimos números:", ultimos_3)
print("Dobro dos pares: ", dobro_dos_pares)
