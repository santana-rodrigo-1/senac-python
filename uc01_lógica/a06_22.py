SALDO = 1000
extrato = []


while True:
    print("1 - Saque: ")
    print("2 - Deposito: ")
    print("3 - Consultar saldo: ")
    print("4 - Transferir: ")
    print("5 - Extrato: ")
    print("6 - Sair: ")
    opcao = input("Escolha uma opção: ")

    match  opcao:
        case "1":
            valor = float(input("Valor do saque: R$"))
            if valor <= 0:
                print("Valor inválido. ")
            elif valor > SALDO:
                print("Valor maior que o saldo:")
            else:
                SALDO = SALDO - valor
                extrato.append(f"Saque: R$ {valor}")
                print(f"Saque realizado, saldo = {SALDO}")
        case "2":
            valor = float(input("Valor do deposito: R$ "))
            if valor > 0:
                SALDO = SALDO + valor
                extrato.append(f"Deposito: R$ {valor}")
                print(f"Deposito realizado - saldo atualizado R$ {SALDO}")
        case "3":
            print(f"Saldo disponivel R$ {SALDO}")
        case "4":
            favorecido = input("Informe o nome: ")
            valor = float(input("Informe o valor da transferencia: "))

            if valor <= 0:
                print("valor invalido")
            elif valor > SALDO:
                print("Saldo insuficiente: ")
            else:
                SALDO = SALDO- valor
                extrato.append(f"Transferencia: Favorecido {favorecido} - valor R$ {valor}")
                print(f"transferencia realizada para {favorecido}")
        case "5":
            print("EXTRATO")
            if len(extrato) == 0:
                print("Nenhuma movimentação")
            else:
                for i in extrato:
                    print(i)
        case "6":
            break
        case _:
            print("Opção invalida")