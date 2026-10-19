vendedores = []

while True:

    print("\n1 - Cadastrar vendedor")
    print("2 - Registrar venda")
    print("3 - Encerrar expediente")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome do vendedor: ")
        vendedores.append(nome)

        print("Vendedor cadastrado com sucesso!")

    elif opcao == "2":

        if len(vendedores) == 0:
            print("Cadastre pelo menos um vendedor primeiro!")
            continue

        print("\nVendedores:")

        for i in range(len(vendedores)):
            print(f"{i+1} - {vendedores[i]}")

        vendedor = int(input("Escolha o vendedor: "))

        valor = float(input("Valor da venda: R$ "))

        print("Venda registrada!")

    elif opcao == "3":
        break

    else:
        print("Opção inválida!")
