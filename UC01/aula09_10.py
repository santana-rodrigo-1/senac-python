# Exercício 4 - Desafio: Controle de Preços

produtos = []
precos = []

qtd_produtos = int(input("Quantos produtos? "))
for i in range(qtd_produtos):
    produto = input(f"Produto {i+1}: ")
    preco = float(input(f"preço {i+1}: "))

    produtos.append(produto)
    precos.append(preco)

print("Quantidade de produtos:", len(produtos))
print("Soma dos preços:", sum(precos))
print("Maior preço:", max(precos))
print("Menor preço:", min(precos))

# PRINTS ABAIXO POR IA:

print("\n--- LISTA DE PRODUTOS ---")
for i in range(len(produtos)):
    print(f"{produtos[i]} - R$ {precos}")
    

print("\n--- ESTATÍSTICAS ---")
print(f"Total de produtos: {len(produtos)}")
print(f"Soma dos preços: R$ {sum(precos):.2f}")
print(f"Média dos preços: R$ {sum(precos) / len(precos):.2f}")
print(f"Maior preço: R$ {max(precos):.2f}")
print(f"Menor preço: R$ {min(precos):.2f}")

print("\n--- PREÇOS EM ORDEM CRESCENTE ---")
print(sorted(precos))

print("\n--- PREÇOS EM ORDEM DECRESCENTE ---")
print(sorted(precos, reverse=True))

# Pesquisa de preço
preco_pesquisa = float(input("\nDigite um preço para pesquisar: "))
quantidade = precos.count(preco_pesquisa)

print(f"O preço R$ {preco_pesquisa:.2f} aparece {quantidade} vez(es) na lista.")