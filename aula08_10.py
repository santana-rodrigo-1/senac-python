# Jogo de advinhação

import random

def novo_numero():
    return random.randint(1, 10)

secreto =  novo_numero(); tentativas = 0

while True:
    palpite = int(input("palpite: "))
    tentativas += 1

    if palpite == secreto:
        print(f"🎉 {tentativas} tentativa(s)"); # 🎉 U+1F389
        break
    elif palpite < secreto: print("Mais alto ↑") # ↑ U+2191
    else: print("Mais baixo ↓") # ↓ U+2193
