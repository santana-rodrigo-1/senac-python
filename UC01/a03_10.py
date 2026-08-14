# Semanas.
# Converta dias em semanas completas e dias restantes.
# dias // 7
# dias % 7

dias = int(input("\nDigite a quantidade de dias: "))

print(f"\n{'CALCULADORA DE SEMANAS':=^40}\n")
print(f"Quantidade de dias:\t| {dias} dia(s)")
print(f"Soma em semanas:\t| {dias //7} semana(s)")
print(f"Sobram:\t\t\t| {dias % 7} dia(s)")
print(f"{"=" * 40}\n")
