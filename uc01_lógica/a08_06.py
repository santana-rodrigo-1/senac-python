#real_para_dolar(v, cot=5.20)

def real_para_dolar(valor, cotacao=5.20):
    return valor / cotacao

print(f"USS {real_para_dolar(520) :.2f}")