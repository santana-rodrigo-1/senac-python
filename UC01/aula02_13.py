# 4. Solicite o ano de nascimento do usuário e calcule sua idade aproximada
# utilizando o ano atual (2026).
# Exemplo:
# Ano de nascimento: 1998
# Sua idade aproximada é 28 anos.

ano_atual = int(input(f"\n\nDigite o ano atual: "))
ano_nasc  = int(input(f"Digite o ano de seu nascimento: "))

idade = ano_atual - ano_nasc

print(f"\nSua idade aproximada é {idade} anos.\n\n")
