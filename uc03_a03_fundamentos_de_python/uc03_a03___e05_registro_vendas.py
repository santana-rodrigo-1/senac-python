print("=" * 40)
print("CONTROLE DE VENDAS JWC")
print("=" * 40)

# Cadastro de vendedores
vendedores = []

qtd = int(input("Quantos vendedores deseja cadastrar? "))

for i in range(qtd):
    nome = input(f"Digite o nome do vendedor {i + 1}: ")
    vendedores.append(nome)

# Estatísticas gerais
quantidade_vendas = 0
valor_total = 0

dinheiro = 0
pix = 0
cartao = 0

maior_venda = 0
menor_venda = 0

# Controle por vendedor
vendas_vendedores = {}

for vendedor in vendedores:
    vendas_vendedores[vendedor] = 0

while True:

    print("\n" + "=" * 40)
    print("MENU")
    print("=" * 40)
    print("1 - Registrar venda")
    print("2 - Encerrar expediente")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\nVendedores cadastrados:")

        for i in range(len(vendedores)):
            print(f"{i + 1} - {vendedores[i]}")

        while True:
            escolha = int(input("Escolha o vendedor: "))

            if 1 <= escolha <= len(vendedores):
                vendedor_atual = vendedores[escolha - 1]
                break

            print("Vendedor inválido!")

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

    elif opcao == "2":

        print("\n" + "=" * 40)
        print("RESUMO DO EXPEDIENTE")
        print("=" * 40)

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

        print("\nExpediente encerrado!")
        break

    else:
        print("Opção inválida!")