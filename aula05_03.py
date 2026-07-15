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
            print("Valor inválido.")
        elif valor > SALDO:
            print("Valor maior que o saldo.")
        else:
            SALDO = SALDO - valor
            print(f"saque realizado, saldo = {SALDO}")

    case "2":
        valor = float(input("valor do depósito: R$"))
        if valor > 0:
            SALDO = SALDO + valor
            print(f"Depósito realizado  - salto atual: R$ {SALDO}")

    case "3":
       print(f"Saldo disponível: {SALDO}")

    case "4":
        print("Programa encerrado.")

    case _:
        print ("Opção inválida.")
