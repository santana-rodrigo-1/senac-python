# 1. ENTRADA DE DADOS
dias = int(input("\nDigite a quantidade de dias: "))

# 2. LÓGICA
semanas = dias // 7
restante = dias % 7

# 3. SAÍDA DE DADOS (Texto à esquerda '<' e Resultado à direita '>')
print(f"\n{'CALCULADORA DE SEMANAS':=^40}\n")

# Reservamos 25 espaços para o texto (à esquerda) e 12 espaços para o resultado (à direita)
print(f"{'Quantidade de dias:':<25} | {f'{dias} dia(s)':>12}")
print(f"{'Soma em semanas:':<25} | {f'{semanas} semana(s)':>12}")
print(f"{'Sobram:':<25} | {f'{restante} dia(s)':>12}")

print(f"\n{'=' * 40}\n")