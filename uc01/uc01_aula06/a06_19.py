# menu do Sistema

SALDO = 1000

extrato = []
depositos = 0
saques = 0
transferencias = 0
total_movimentado = 0

while True:
    print("1 - Saque")
    print("2 - Depósito")
    print("3 - Consultar saldo")
    print("4 - Transferência")
    print("5 - Extrato")
    print("6 - Sair")
    print("7 - Cancelar")

    opcao = input("Escolha uma opção: ")

    match  opcao:

        case "1": # Saque
            valor = float(input("Valor do saque: R$ "))
            if valor <= 0 or valor > 1500:
                print("Valor inválido. ")
            elif valor > SALDO:
                print("Valor maior que o saldo:")
            else:
                SALDO = SALDO - valor
                saques +=1
                total_movimentado += valor
                extrato.append(f"Saque: R$ {valor}")
                print(f"Saque realizado, saldo = {SALDO}")

        case "2": # Depósito
            valor = float(input("Valor do deposito: R$ "))
            if valor > 0:
                SALDO = SALDO + valor
                depositos +=1
                total_movimentado += valor
                extrato.append(f"Depósito: R$ {valor}")
                print(f"Deposito realizado - saldo atualizado R$ {SALDO}")

        case "3": # Consultar saldo
            extrato.append(f"Saldo: R$ {valor}")
            print(f"Saldo disponivel R$ {SALDO}")

        case "4": # Transferência
            tax_transf = 5.00
            print(f"OBS: Transferências possuem uma taxa de: R$ {tax_transf:.2f}")
            favorecido = input("Digite nome do favorecido: ").upper()
            valor = float(input("Valor do transferência: R$ "))
            if valor <= 0:
                print("Valor inválido.")
            elif valor > SALDO:
                print("Saldo insuficiente.")
                print(f"Seu saldo atual é: R$ {SALDO}")
            else:
                SALDO = SALDO - valor
                transferencias += 1
                total_movimentado += valor
                extrato.append(f"Transferencia: favorecido {favorecido} - Valor R$ {valor}")
                print(f"Transferência realizada para {favorecido}")
                print(f"Seu saldo atual é: R$ {SALDO - tax_transf}")

        case "5": # Extrato
            print("\nEXTRATO\n")
            if len(extrato) == 0:
                print("Nenhuma movimentação.")
            else:
                for i in extrato:
                    print(i)
        
        case "6": # Sair
            print("\nRESUMO\n")
            print(f"SALDO FINAL: R$ {SALDO}")
            print(f"DEPOSITOS REALIZADOS: {depositos}")
            print(f"SAQUES REALIZADOS: {saques}")
            print(f"TRANSFERÊNCIAS: {transferencias}")
            print(f"TOTAL MOVIMENTADO: {total_movimentado}\n")
            break              

        case "7": # Cancelar
            break

        case _:
            print("\nOpção invalida!")
