"""
Exercício 5 (CRUD Básico em Lista: Create & Read)
Crie uma classe Pet (nome, especie).
• Monte um menu com while True permitindo Cadastrar (Create) e Listar
(Read) os pets da lista.
"""

class Pet:
    def __init__(self):
        self.nome
        self.especie

    def __str__(self):
        return f"pet: {self.nome} | Espécie: {self.especie}"

lista_pets = []

while True:
    print()
    print("=== MENU PET ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do pet: ")
        especie = input("Espécie: ")
        novo=pet = Pet(nome, especie)
        lista_pets.append(novo_pet)
        print(f"pet {nome} cadastrado com sucesso!")
    if opcao == "2":
        print("lista de pets cadastrados")
        if not lista_pets:
            print("Nenhum pet cadastrado")
        else:
            for i, pet in enumerate(lista_pets,1):
                print(f"{i} - {pet}")
    if opcao == "0":
        print("Saindo do sistema")
        break
    else:
        print("opção inválida")

"""
# RESPOSTA POR IA

class Pet:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

pets = []

while True:
    print()
    print("=== MENU PET ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do pet: ")
        especie = input("Espécie: ")

        pet = Pet(nome, especie)
        pets.append(pet)

        print("Pet cadastrado com sucesso!")

    elif opcao == "2":
        print()
        print("=== LISTA DE PETS ===")

        for pet in pets:
            print(f"Nome: {pet.nome} | Espécie: {pet.especie}")

    elif opcao == "3":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
"""
