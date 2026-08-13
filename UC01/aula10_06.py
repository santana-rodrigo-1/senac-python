vendas = [[1500, 2000, 1800, 2200],
          [1100, 2800, 3100, 3500],
          [3000, 2800, 3100, 3500]
          ]

print("MATRIZ DE VENDAS")
print("Semana 1, Semana 2, Semana 3, Semana 4")

for i in range(len(vendas)):
    print(f"Vendedor {i+1}", end = " ")
    for j in range (len(vendas[i])):
        print(f"R$ {vendas[i][j]}", end = " ")
        print()
    print()

print("Faturamento total por semana")
print()
colunas = len(vendas[0])
totais_semanas = []
for c in range(colunas):
    total_semana = 0
    for v in range(len(vendas)):
        total_semana += vendas[v][c]

        totais_semanas.append(total_semana)
        print(f"Semana {c+1}: R$ {total_semana}")
        print()

print("Semana de maior faturamento")
maior_faturamento = max(totais_semanas)
maior_semana = totais_semanas.index(maior_faturamento)
print(f"Maior faturamento: R$ {maior_faturamento} - "
      f"Semana {maior_semana+1}"
      )

print("\n Total vendido pelo vendedor 1")
vendedor_1 = 
