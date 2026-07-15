# 7 — Calculadora de IMC
# Peça o peso (em kg) e a altura (em metros) do usuário e calcule o IMC,
# com a fórmula: IMC = peso / (altura × altura).
# Depois, exiba uma mensagem: "Abaixo do peso" se o IMC for menor que 18.5; "Peso ideal" se estiver
# entre 18.5 e 24.9; "Acima do peso" se for 25 ou mais.
# Dica: Esse exercício tem três faixas de resultado — por isso você vai
# precisar de um elif no meio, entre o if e o else.

v01 = float(input("\nDigite seu peso em Kg: "))
v02 = float(input("Digite sua altura em metros: "))

IMC = v01 / (v02 * v02) # (peso / (altura × altura))

print(f"Seu IMC é: {IMC}")
if IMC < 18.5:
    print("Você esta Abaixo do peso.")
elif IMC >= 25:
    print("Você esta Acima do peso.")
else:
    print("Você esta no Peso ideal.")
