# LISTA DE EXERCÍCIOS – ENTRADA DE DADOS, CÁLCULOS E SAÍDA EM PYTHON.

# 1. Crie um programa que solicite ao usuário a cidade onde ele mora
# e exiba a mensagem: Você mora em [cidade].

cidade = input("\nDigite a cidade onde mora: ").strip().upper()

print(f"\nVocê mora em {cidade}.")
print(f"\n+{"-" * 30}+\n")

# .strip()      -> Remove os espaços em branco inúteis do início e do fim.
# .title()      -> Coloca a primeira letra de CADA palavra em maiúscula (Ex: Rio De Janeiro).
# .capitalize() -> Coloca APENAS a primeira letra do texto em maiúscula (Ex: Rio de janeiro).
# .upper()      -> Deixa o texto INTEIRO EM MAIÚSCULO (Ex: RIO DE JANEIRO).
# .lower()      -> Deixa o texto inteiro em minúsculo (Ex: rio de janeiro).
