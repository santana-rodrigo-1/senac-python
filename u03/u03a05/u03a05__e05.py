'''
EXERCÍCIO 1 - CADASTRO DE PRODUTOS
Python • Arquivos TXT + Funções
'''

import os

ARQUIVO = "produtos.txt"
# Abaixo opção de salvamento por pasta substituto do: ARQUIVO = "produtos.txt"
# ARQUIVO = "C:\Users\santana.rodrigo\OneDrive - SENAC RIO\senac\senac_python\u03\u03a05\u03a05__e05.py"

def cadastrar():
    nome = input("Nome do produto: ")

    while True:
        try:
            preco = float(input("Preço: "))
            break
        except ValueError:
            print("Digite um número válido!")

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            break
        except ValueError:
            print("Digite um número inteiro válido!")

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{preco};{quantidade}\n")

    print()
    print("Produto cadastrado com sucesso!")
    print(f"Produto: {nome}")
    print(f"Preço: {preco}")
    print(f"quantidade: {quantidade}")

def listar_produtos():
    if not os.path.exists(ARQUIVO):
        print("Nenhum produto cadastrado.")
        return

    print("\n===== PRODUTOS CADASTRADOS =====")

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")

            print(f"Produto: {nome}")
            print(f"Preço: R$ {float(preco):.2f}")
            print(f"Quantidade: {quantidade}")
            print("-" * 30)


def contar():
    if not os.path.exists(ARQUIVO):
        return 0

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        produtos = arquivo.readlines()

    return len(produtos)


def excluir():
    if not os.path.exists(ARQUIVO):
        print("Nenhum cadastro encontrado.")
        return

    resposta = input("Deseja realmente excluir todos os produtos? (s/n): ")

    if resposta.lower() == "s":
        os.remove(ARQUIVO)
        print("Todos os produtos foram excluídos!")
    else:
        print("Operação cancelada.")


while True:
    print("\n===== SISTEMA DE PRODUTOS =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar quantidade de produtos")
    print("4 - Excluir cadastro")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        total = contar()
        print(f"Total de produtos cadastrados: {total}")

    elif opcao == "4":
        excluir()

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")