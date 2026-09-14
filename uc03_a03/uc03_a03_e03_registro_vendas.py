'''
Sistema de Controle de Caixa JWC
'''


class registro_vendas:
    def __init__(self):
        self.registrar_venda
        self.modelo
        self.hora_entrada

    def __str__(self):
        return f"Placa: {self.placa} | Modelo: {self.modelo} | Hora de entrada: {self.hora_entrada}"

lista_estacionamento= []

print('=' * 30)
print('CONTROLE DE VENDAS'.center(30))
print('=' * 30)
print()
vendedor = input("Digite o nome do vendedor: ").strip

while True:
    print('=' * 30)
    print("1 - Registrar venda")
    print("1 - Encerrar expediente")
    print("3 - Sair")
    print('=' * 30)

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