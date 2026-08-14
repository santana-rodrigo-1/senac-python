SALDO = 1000

while True:
    print("1 - Saque: ")
    print("2 - Deposito: ")
    print("3 - Consultar saldo: ")
    print("4 - Cancelar: ")

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
                print(f"Saque realizado, saldo = {SALDO}")
        case "2":
            valor = float(input("Valor do deposito: R$ "))
            if valor > 0:
                SALDO = SALDO + valor
                print(f"Deposito realizado - saldo atualizado R$ {SALDO}")
        case "3":
            print(f"Saldo disponivel R$ {SALDO}")
        case "4":
            print("Programa encerrado")
        case _:
            print("Opção invalida")
         