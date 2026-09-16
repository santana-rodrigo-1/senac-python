# ⚡Crie ContaPoupanca(ContaCorrente) com um método render().
# + Lista da UC1 (Objetos, Classes, Métodos, Herança, Métodos Especiais)

class ContaCorrente:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depositado: R${valor:.2f}. Novo saldo: R${self.saldo:.2f}')
        else:
            print('Valor de depósito deve ser positivo.')

conta = ContaCorrente("João", 1000)

conta.depositar(500)  # Deposita R$500

print(f'Saldo atual: R${conta.saldo:.2f}')  # Exibe o saldo atual