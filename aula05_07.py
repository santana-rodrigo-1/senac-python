print("\nBem-vindo!")
print("Digite uma opção:")
print("1 - Caixa eletrônico.")
print("2 - Empréstimo bancário.")
print("3 - Bolsa de estudos")
print("4 - Pedra, papel e tesoura")
print("5 - Sair")

opcao = input("Escolha uma opção: ")

match opcao:
    case "1":
        print("\nBem-vindo!")
        print("Digite uma opção:")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Consultar saldo")
        print("4 - Sair")

        SALDO = 1000
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                valor = float(input("valor do saque: R$"))
                if valor < 0:
                    print("Valor inválido.\n")
                elif valor > SALDO:
                    print("Valor maior que o saldo.\n")
                else:
                    SALDO = SALDO - valor
                    print(f"saque realizado, saldo = R$ {SALDO}.\n")

            case "2":
                valor = float(input("valor do depósito: R$"))
                if valor > 0:
                    SALDO = SALDO + valor
                    print(f"Depósito realizado  - salto atual: R$ {SALDO}.\n")

            case "3":
                print(f"Saldo disponível: R$ {SALDO}.\n")

            case "4":
                print("Programa encerrado.\n")

            case _:
                print ("Opção inválida.\n")
    
    case "2":
        renda = float(input("\nDigite sua renda: R$ "))
        score = float(input("Digite seu score: "))

        if renda >= 3000 and score >= 700:
            print("\nEmpréstimo aprovado.\n")
        else:
            print("\nEmpréstimo negado.\n")
    
    case "3":
        media = float(input("\nDigite a média: "))
        renda_familiar = float(input("Digite a renda em R$: "))

        if media >= 9 or renda_familiar <= 2000:
            print("\nBolsa aprovada.\n")
        else:
            print("\nBolsa negada.\n")

    case "4":
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

    case "5":
        print("Programa encerrado.\n")

    case _:
        print ("Opção inválida.\n")
