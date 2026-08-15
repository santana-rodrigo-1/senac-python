"""
DESAFIO EXTRA (BONUS): Estacionamento VIP JWC Tech
A História do Desafio:
"A diretoria da empresa JWC Tech precisa de um sistema rápido no terminal para
controlar os carros estacionados na garagem da sede."
Enunciado para os Alunos:
1. Crie a classe VeiculoEstacionado:
• Atributos: placa, modelo e hora_entrada (número inteiro, ex: 8 para 8h da
manhã).
• Método __str__: Exibe a placa, o modelo e o horário de entrada
formatados.
• Método calcular_pagamento(hora_saida):
• A tarifa do estacionamento é R$ 10,00 por hora.
• Calcule quantas horas o carro ficou (hora_saida - hora_entrada).
• Retorne o valor total a ser pago.

2. Crie o Menu em Loop (while True):
• 1 - [C] Registrar Entrada de Veículo: Pede a placa, o modelo e a hora de
entrada.
• 2 - [R] Listar Veículos Estacionados: Mostra todos os carros na garagem.
• 3 - [D] Registrar Saída e Cobrar Pagamento: Pede a placa do veículo,
pede o horário de saída, calcula o valor a pagar, exibe o recibo e remove o
veículo da garagem!
• 0 - Sair do Sistema.
"""

class VeiculoEstacionado:
    def __init__(self):
        self.placa
        self.modelo
        self.hora_entrada

    def __str__(self):
        return f"Placa: {self.placa} | Modelo: {self.modelo} | Hora de entrada: {self.hora_entrada}"

lista_estacionamento= []

while True:
    print()
    print("ESTACIONAMENTO VIP JWC TECH")
    print("========= CADASTRO ========")
    print("1 - Entrada")
    print("2 - Listar")
    print("3 - registrar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        hora_entrada = input("Hora de entrada: ")

        

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