def depositar(saldo, valor):
    return saldo + valor

saldo = 1000
saldo =  depositar(saldo, 500)
print(f"saldo: R$ {saldo:.2f}")
