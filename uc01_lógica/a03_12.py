# CALCULADORA DE SEMANAS

# 1. ENTRADA DE DADOS
dias = int(input("\nDigite a quantidade de dias: "))

# 2. LÓGICA / PROCESSAMENTO
semanas = dias // 7
restante = dias % 7

# 3. SAÍDA / INTERFACE
LARGURA = 60
ESPACO_ESQUERDA = 22
ESPACO_DIREITA = LARGURA - ESPACO_ESQUERDA - 5

print(f"\n{' CALCULADORA DE SEMANAS ':=^{LARGURA}}")

txt_dias = f"{dias:,} dias"
txt_sem = f"{semanas:,} sem."
txt_rest = f"{restante:,} dias"

print(f"| {'Quantidade de dias:':<{ESPACO_ESQUERDA}} {txt_dias:>{ESPACO_DIREITA}} |")
print(f"| {'Soma em semanas:':<{ESPACO_ESQUERDA}} {txt_sem:>{ESPACO_DIREITA}} |")
print(f"| {'Sobram:':<{ESPACO_ESQUERDA}} {txt_rest:>{ESPACO_DIREITA}} |")

print(f"{'=' * LARGURA}\n")
