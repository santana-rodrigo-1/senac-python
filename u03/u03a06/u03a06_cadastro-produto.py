import os

ARQUIVO = "produtos.txt"


def cadastrar_produto():

    print()
    print("===== CADASTRAR PRODUTO =====")

    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade: "))

    with open(ARQUIVO, "a") as arquivo:
        arquivo.write(f"{nome};{preco};{quantidade}\n")

    print("Produto cadastrado com sucesso!")


def listar_produtos():

    print()
    print("===== PRODUTOS CADASTRADOS =====")

    if not os.path.exists(ARQUIVO):
        print("Nenhum produto cadastrado.")
        return

    with open(ARQUIVO, "r") as arquivo:

        encontrou = False

        for linha in arquivo:

            dados = linha.strip().split(";")

            nome = dados[0]
            preco = float(dados[1])
            quantidade = int(dados[2])

            print()
            print("Produto:", nome)
            print(f"Preço: R$ {preco:.2f}")
            print("Quantidade:", quantidade)

            encontrou = True

        if not encontrou:
            print("Nenhum produto cadastrado.")


def consultar_quantidade():

    if not os.path.exists(ARQUIVO):
        return 0

    quantidade = 0

    with open(ARQUIVO, "r") as arquivo:

        for linha in arquivo:
            if linha.strip():
                quantidade += 1

    return quantidade


def excluir_cadastro():

    print()
    resposta = input("Tem certeza que deseja excluir todos os produtos? (s/n): ")

    if resposta.lower() == "s":

        if os.path.exists(ARQUIVO):

            os.remove(ARQUIVO)

            print("Cadastro excluído com sucesso!")

        else:

            print("O arquivo não existe.")

    else:

        print("Operação cancelada.")


# Programa principal

while True:

    print()
    print("==============================")
    print("     SISTEMA DE PRODUTOS")
    print("==============================")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar quantidade de produtos")
    print("4 - Excluir cadastro")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        cadastrar_produto()

    elif opcao == "2":

        listar_produtos()

    elif opcao == "3":

        total = consultar_quantidade()

        print()
        print("Total de produtos cadastrados:", total)

    elif opcao == "4":

        excluir_cadastro()

    elif opcao == "5":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")
