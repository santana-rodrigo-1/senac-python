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
    elif opcao == "11"
        break
    else _:
        print("\nOpção invalida!") 




"""      
        case "10": # Sair
            print("\nRESUMO\n")
            print(f"SALDO FINAL: R$ {SALDO}")
            print(f"DEPOSITOS REALIZADOS: {depositos}")
            print(f"SAQUES REALIZADOS: {saques}")
            print(f"TRANSFERÊNCIAS: {transferencias}")
            print(f"TOTAL MOVIMENTADO: {total_movimentado}\n")
            break              
"""