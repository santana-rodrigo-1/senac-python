# Empréstimo Bancário (and)
# O empréstimo será aprovado apenas se o cliente atender aos dois requisitos:
# renda mínima e score mínimo.
# renda >= 3000 and score >= 700

renda = float(input("\nDigite sua renda: R$ "))
score = float(input("Digite seu score: "))

if renda >= 3000 and score >= 700:
    print("\nEmpréstimo aprovado.\n")
else:
    print("\nEmpréstimo negado.\n")
