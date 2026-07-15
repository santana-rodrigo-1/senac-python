# Caixa Eletrônico JWC Bank

SALDO = 1000.00
SENHA = "senac2026"

senha = input("Senha: ")

if senha == SENHA:
    valor = float(input("Saque: "))

    if valor <= 0:
        print("Valor inválido.")
    elif valor > SALDO:
        print("Saldo insuficiente.")
    elif valor % 10 != 0:
        print("Só notas de R$10.")
    else:
        print("Saque realizado!")
else:
    print("Senha incorreta.")
