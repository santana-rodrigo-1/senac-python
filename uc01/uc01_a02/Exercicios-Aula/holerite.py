# Holerite simples 

nome = input("Funcionário: ") 
salario = float(input("Salário bruto: R$ ")) 
INSS = 0.11                       # 11% 
desconto = salario * INSS 
liquido = salario - desconto 

print(f"\n--- HOLERITE: {nome} ---") 
print(f"Bruto:    R$ {salario:.2f}") 
print(f"INSS (11%): -R$ {desconto:.2f}") 
print(f"Líquido:  R$ {liquido:.2f}") 