# DESAFIO FINAL - SISTEMA DE ALUNOS
# Python · Funções + Listas + Menu + while + if/elif
# Crie um sistema para cadastrar e gerenciar alunos e suas notas.

nomes = []
notas = []

def cadastrar_aluno():
    nome_aluno = input(f"Nome do aluno: ")
    nota_aluno = int(input(f"Nota do aluno: "))

    nomes.append(nome_aluno)
    notas.append(nota_aluno)

print("Aluno(s) cadastrado(s) com sucesso!")

def listar_aluno():
    print("Alunos")
    for i in range(len(nomes)):
        print(f"{i+1 - {nomes}} | Nota: {notas[i]}")

def maior_nota():
    maior = max(notas)
    indice = notas.index(maior)

    print(f"maior nota: {maior}")
    print(f"Aluno: {nomes[indice]}")



while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Maior nota")
    print("4 - Menor nota")
    print("5 - Calcular média")
    print("6 - Mostrar aprovados")
    print("7 - Remover aluno")
    print("8 - Ordenar alunos")
    print("9 - Relatório da turma")
    print("10 - Sair")
    print("11 - Cancelar")


    opcao = input("Escolha uma opção: ")

    if opcao == "1"
        cadastrar_aluno()
    elif opcao == "2"
        listar_aluno()
    elif opcao == "3"
        maior_nota()
    elif opcao == "4"

    elif opcao == "5"

    elif opcao == "6"

    elif opcao == "7"

    elif opcao == "8"

    elif opcao == "9"

    elif opcao == "10"
        print
    elif opcao == "11" # Cancelar
        break
    else _:
        print("\nOpção invalida!") 





    match  opcao:

        case "1": # Cadastrar aluno


            

        case "2": # Listar alunos
                



            valor = float(input("Valor do deposito: R$ "))
            if valor > 0:
                SALDO = SALDO + valor
                depositos +=1
                total_movimentado += valor
                extrato.append(f"Depósito: R$ {valor}")
                print(f"Deposito realizado - saldo atualizado R$ {SALDO}")

        case "3": # Consultar saldo
            extrato.append(f"Saldo: R$ {valor}")
            print(f"Saldo disponivel R$ {SALDO}")

        case "4": # Transferência
            tax_transf = 5.00
            print(f"OBS: Transferências possuem uma taxa de: R$ {tax_transf:.2f}")
            favorecido = input("Digite nome do favorecido: ").upper()
            valor = float(input("Valor do transferência: R$ "))
            if valor <= 0:
                print("Valor inválido.")
            elif valor > SALDO:
                print("Saldo insuficiente.")
                print(f"Seu saldo atual é: R$ {SALDO}")
            else:
                SALDO = SALDO - valor
                transferencias += 1
                total_movimentado += valor
                extrato.append(f"Transferencia: favorecido {favorecido} - Valor R$ {valor}")
                print(f"Transferência realizada para {favorecido}")
                print(f"Seu saldo atual é: R$ {SALDO - tax_transf}")

        case "5": # Extrato
            print("\nEXTRATO\n")
            if len(extrato) == 0:
                print("Nenhuma movimentação.")
            else:
                for i in extrato:
                    print(i)
        
        case "10": # Sair
            print("\nRESUMO\n")
            print(f"SALDO FINAL: R$ {SALDO}")
            print(f"DEPOSITOS REALIZADOS: {depositos}")
            print(f"SAQUES REALIZADOS: {saques}")
            print(f"TRANSFERÊNCIAS: {transferencias}")
            print(f"TOTAL MOVIMENTADO: {total_movimentado}\n")
            break              

        case "11": # Cancelar
            break

        case _:
            print("\nOpção invalida!")
