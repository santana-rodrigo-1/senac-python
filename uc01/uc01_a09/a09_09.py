# Exercício 3 - Lista de Compras

compras = ["arroz", "feijão", "macarrão", "leite", "café"]

print(compras)
print("Primeiro item: ", compras[0])
print("Último item: ", compras[-1])
print("Total de itens", len(compras))

print(compras)
posicao = compras.index("macarrão")
compras.remove("macarrão")
print(compras)
compras.insert(posicao, "carne")
print(compras)
compras.append("macarrão")
print(compras)
compras.sort()
print(compras)
