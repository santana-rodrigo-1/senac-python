def calcular_media(n1, n2):
    return (n1 + n2) / 2

def situacao(media):
    if media >=7: return "Aprovado"
    elif media >=5: return "Recup"
    else: return "Reprovdo"

m = calcular_media(8, 6) #7.0
print(situacao(m)) #Aprovado
