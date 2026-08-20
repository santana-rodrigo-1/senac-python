def depositar(saldo, valor):
    return saldo + valor

def sacar(saldo, valor):
    if valor > saldo:
        print("Saldo insificiente")
        return saldo
    return saldo - valor

def extrato(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")

saldo = 0
while True:
    print("1 - depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Valor: "))
        saldo = depositar(saldo, valor)
    elif opcao == "2":
        valor = float(input("Valor: "))
        saldo = sacar(saldo, valor)
    elif opcao == "3":
        extrato(saldo)
    elif opcao == "4":
        break
    else:
        print("opção inválida")
