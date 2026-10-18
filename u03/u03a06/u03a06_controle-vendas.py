print("==============================")
print("      CONTROLE DE VENDAS")
print("==============================")

vendedor = input("Digite o nome do vendedor: ")

quantidade_vendas = 0
valor_total = 0

dinheiro = 0
pix = 0
cartao = 0

maior_venda = 0
menor_venda = 0

while True:

    print()
    print("1 - Registrar venda")
    print("2 - Encerrar expediente")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        # Validação do valor
        while True:
            valor = float(input("Digite o valor da venda: R$ "))

            if valor > 0:
                break
            else:
                print("Valor inválido! Digite um valor maior que zero.")

        # Forma de pagamento
        while True:
            print()
            print("Forma de pagamento")
            print("1 - Dinheiro")
            print("2 - Pix")
            print("3 - Cartão")

            pagamento = input("Escolha a forma de pagamento: ")

            if pagamento == "1":
                dinheiro += 1
                break

            elif pagamento == "2":
                pix += 1
                break

            elif pagamento == "3":
                cartao += 1
                break

            else:
                print("Forma de pagamento inválida!")

        # Contadores e acumuladores
        quantidade_vendas += 1
        valor_total += valor

        # Maior e menor venda
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
        break

    else:
        print("Opção inválida!")


# Resumo
print()
print("==============================")
print("      RESUMO DO EXPEDIENTE")
print("==============================")

print("Vendedor:", vendedor)
print("Quantidade de vendas:", quantidade_vendas)
print(f"Valor total vendido: R$ {valor_total:.2f}")
print("Dinheiro:", dinheiro, "vendas")
print("Pix:", pix, "vendas")
print("Cartão:", cartao, "vendas")

if quantidade_vendas > 0:
    print(f"Maior venda: R$ {maior_venda:.2f}")
    print(f"Menor venda: R$ {menor_venda:.2f}")
else:
    print("Nenhuma venda registrada.")
