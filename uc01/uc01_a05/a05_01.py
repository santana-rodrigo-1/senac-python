print("1 - Carro popular: ")
print("2 - Carro Sedan: ")
print("3 - Carro SUV: ")
print("4 - Cancelar: ")

opcao = input("Escolha um veículo: ")

match opcao:
    case "1":
        dias = int(input("Quantidade de dias: "))
        if dias >= 1:
            print("Carro popular reservado!")
        else:
            print("Quantidade de dias inválido")
    case "2":
        dias = int(input("Quantidade de dias: "))
        if dias >= 1:
            print("Carro Sedan reservado!")
        else:
            print("Quantidade de dias inválido")
    case "3":
        dias = int(input("Quantidade de dias: "))
        if dias >= 1:
            print("Carro SUV reservado!")
        else:
            print("Quantidade de dias inválido")
    case "4":
        print("Reserva cancelada.")
