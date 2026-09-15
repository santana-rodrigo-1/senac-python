
jogador1 = input("Jogador 1 - Escolha pedra, papel ou tesoura: ")
jogador2 = input("Jogador 2 - Escolha pedra, papel ou tesoura: ")

match jogador1:
    case "pedra":
        if jogador2 == "pedra":
            print("Empate!")
        elif jogador2 == "tesoura":
            print("Jogador 1 venceu!")
        elif jogador2 == "papel":
            print("Jogador 2 venceu!")
        else:
            print("Jogada do jogador 2 inválida.")
            
match jogador1:
    case "papel":
        if jogador2 == "pedra":
            print("Jogador 2 venceu!")
        elif jogador2 == "tesoura":
            print("Jogador 1 venceu!")
        elif jogador2 == "papel":
            print("Empate!")
        else:
            print("Jogada do jogador 2 inválida.")

match jogador1:
    case "tesoura":
        if jogador2 == "pedra":
            print("Jogador 2 venceu!")
        elif jogador2 == "tesoura":
            print("Empate!")
        elif jogador2 == "papel":
            print("Jogador 1 venceu!")
        else:
            print("Jogada do jogador 2 inválida.")
