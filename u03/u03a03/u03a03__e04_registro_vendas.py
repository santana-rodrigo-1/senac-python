print("=" * 30)
print("CONTROLE DE VENDAS".center(30))
print("=" * 30)

vendedor = input("Digite o nome do vendedor: ")

quantidade_vendas = 0
valor_total = 0

dinheiro = 0
pix = 0
cartao = 0

maior_venda = 0
menor_venda = 0

while True:
    print("\n1 - Registrar venda")
    print("2 - Encerrar expediente")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        while True:
            valor = float(input("Digite o valor da venda: R$ "))

            if valor > 0:
                break
            else:
                print("Valor inválido! Digite um valor maior que zero.")

        print("\nForma de pagamento")
        print("1 - Dinheiro")
        print("2 - Pix")
        print("3 - Cartão")

        while True:
            pagamento = input("Escolha a forma de pagamento: ")

            if pagamento in ("1", "2", "3"):
                break
            else:
                print("Forma de pagamento inválida!")

        quantidade_vendas += 1
        valor_total += valor

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

    elif opcao == "2":
        print("\n" + "=" * 30)
        print("RESUMO DO EXPEDIENTE".center(30))
        print("=" * 30)

        print(f"Vendedor: {vendedor}")
        print(f"Quantidade de vendas: {quantidade_vendas}")
        print(f"Valor total vendido: R$ {valor_total:.2f}")
        print(f"Dinheiro: {dinheiro} vendas")
        print(f"Pix: {pix} vendas")
        print(f"Cartão: {cartao} vendas")

        if quantidade_vendas > 0:
            print(f"Maior venda: R$ {maior_venda:.2f}")
            print(f"Menor venda: R$ {menor_venda:.2f}")
        else:
            print("Nenhuma venda registrada.")

        break

    else:
        print("Opção inválida!")