'''
EXERCÍCIO 1 - CADASTRO DE PRODUTOS
Python • Arquivos TXT + Funções
'''

import os

ARQUIVO = "teste.txt"

def cadastrar():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{preco};{quantidade}\n")
    print(f"Produto '{nome}' cadastrado com sucesso!")


def listar():
    if not os.path.exists(ARQUIVO):
        print("Nenhum nome cadastrado ainda.")
        return
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        nomes = arquivo.readlines()
        print("Nomes cadastrados:")
        for nome in nomes:
            print(nome.strip())
"""

def consultar():
    if os.path.exists(ARQUIVO):
        print'

"""
def excluir():
    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)
        print("Todos os nomes foram excluídos com sucesso!")
    else:
        print("Nenhum nome cadastrado ainda.")

while True:

    print("\n===== MENU DE OPÇÕES =====")    
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Consultar quantidade de produtos")
    print("4. Excluir cadastro")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        consultar()        
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")