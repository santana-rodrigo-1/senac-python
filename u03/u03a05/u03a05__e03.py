import os

ARQUIVO = "teste.txt"

def cadastrar():
    nome = input("Digite o nome a ser cadastrado: ")
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")
    print(f"Nome '{nome}' cadastrado com sucesso!")

def listar():
    if not os.path.exists(ARQUIVO):
        print("Nenhum nome cadastrado ainda.")
        return
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        nomes = arquivo.readlines()
        print("Nomes cadastrados:")
        for nome in nomes:
            print(nome.strip())
def excluir():
    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)
        print("Todos os nomes foram excluídos com sucesso!")
    else:
        print("Nenhum nome cadastrado ainda.")

while True:
    print("\nMenu de opções:")    
    print("1. Cadastrar nome")
    print("2. Listar nomes")
    print("3. Excluir")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        excluir()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")