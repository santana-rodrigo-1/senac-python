vendedores = []
vendas_vendedores = {}

quantidade_vendas = 0
valor_total = 0

dinheiro = 0
pix = 0
cartao = 0

maior_venda = 0
menor_venda = 0

while True:

    print("\n1 - Cadastrar vendedor")
    print("2 - Registrar venda")
    print("3 - Encerrar expediente")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome do vendedor: ")

        vendedores.append(nome)
        vendas_vendedores[nome] = 0

        print("Vendedor cadastrado com sucesso!")

    elif opcao == "2":

        if len(vendedores) == 0:
            print("Cadastre pelo menos um vendedor primeiro!")
            continue

        print("\nVendedores cadastrados:")

        for i in range(len(vendedores)):
            print(f"{i + 1} - {vendedores[i]}")

        escolha = int(input("Escolha o vendedor: "))
        vendedor_atual = vendedores[escolha - 1]

        while True:
            valor = float(input("Digite o valor da venda: R$ "))

            if valor > 0:
                break

            print("Valor inválido! Digite um valor maior que zero.")

        print("\nForma de pagamento")
        print("1 - Dinheiro")
        print("2 - Pix")
        print("3 - Cartão")

        while True:
            pagamento = input("Escolha a forma de pagamento: ")

            if pagamento in ("1", "2", "3"):
                break

            print("Forma de pagamento inválida!")

        quantidade_vendas += 1
        valor_total += valor

        vendas_vendedores[vendedor_atual] += valor

        if pagamento == "1":
            dinheiro += 1
        elif pagamento == "2":
            pix += 1
        else:
            cartao += 1

        if quantidade_vendas == 1:
            maior_venda = valor
            menor_venda = valor
        else:
            if valor > maior_venda:
                maior_venda = valor

            if valor < menor_venda:
                menor_venda = valor

        print("Venda registrada com sucesso!")

    elif opcao == "3":

        print("\nRESUMO DO EXPEDIENTE")

        print(f"Quantidade de vendas: {quantidade_vendas}")
        print(f"Valor total vendido: R$ {valor_total:.2f}")

        print(f"Dinheiro: {dinheiro} vendas")
        print(f"Pix: {pix} vendas")
        print(f"Cartão: {cartao} vendas")

        if quantidade_vendas > 0:
            print(f"Maior venda: R$ {maior_venda:.2f}")
            print(f"Menor venda: R$ {menor_venda:.2f}")

        print("\nTotal vendido por vendedor:")

        for vendedor, total in vendas_vendedores.items():
            print(f"{vendedor}: R$ {total:.2f}")

        break

    else:
        print("Opção inválida!")