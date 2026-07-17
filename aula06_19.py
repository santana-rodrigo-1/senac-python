# menu do Sistema

SALDO = 1000

while True:
    print("1 - Saque")
    print("2 - Deposito")
    print("3 - Consultar saldo")
    print("4 - Transferir")
    print("5 - Cancelar")

    opcao = input("Escolha uma opção: ")

    match  opcao:

        case "1":
            valor = float(input("Valor do saque: R$ "))
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
            input("Digite nome do favorecido: ")
            valor = float(input("Valor do transferência: R$ "))
            if valor <= 0:
                print("Valor inválido. ")
            elif valor > SALDO:
                print("Valor maior que o saldo:")
            else:
                SALDO = SALDO - valor
                print(f"Transferência realizada, saldo atual= {SALDO}")

        case "5":
            break

        case _:
            print("\nOpção invalida!\n")
