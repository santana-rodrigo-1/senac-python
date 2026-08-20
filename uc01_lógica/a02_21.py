# 7. Conversor de Moedas (Desafio)
# Solicite:
# • Um valor em reais.
# • A cotação do dólar.
# • A cotação do euro.
# • A cotação da libra.
# Calcule quanto o valor informado equivale em cada uma dessas moedas.
# Apresente os resultados com duas casas decimais.

real = float(input("\n\nDigite valor em Real: "))
cotacao_dolar = float(input("Digite cotação do Dólar: "))
cotacao_euro = float(input("Digite cotação do Euro: "))
cotacao_libra = float(input("Digite cotação da Libra: "))

dolar_real = real / cotacao_dolar
euro_real = real / cotacao_euro
libra_real = real / cotacao_libra

print(f"\n{"=" * 40}")
print(f"Valor\tem (BRL) Real:\t\tR$ {real:.2f}")
print(f"Cotação\tem (USD) Dólar:\t\tR$ {dolar_real:.2f}")
print(f"Cotação\tem (EUR) Euro:\t\tR$ {euro_real:.2f}")
print(f"Cotação\tem (GBP) Libra:\t\tR$ {libra_real:.2f}")
print(f"{"=" * 40}\n\n")
