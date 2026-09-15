# 3 — Maior de idade
# Peça a idade do usuário. Se for maior ou igual a 18 anos, exiba "Maior de idade". 
# Caso contrário, exiba "Menor de idade".

ano_at = int(input("\nDigite ano atual: "))
ano_na = int(input("Digite ano de nascimento: "))

idade = ano_at - ano_na

print(f"\nIdade: {idade}")
if idade >= 18:
    print("Maior de idade\n")
else:
    print("Menor de idade\n")
  