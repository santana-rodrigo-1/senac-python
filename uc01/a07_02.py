print("=" * 50)
print("SUPERMERCADO")
print("=" * 50)

quantidade = int(input("Quantidade de produtos: "))

produtos = []
precos = []
quantidades = []

for i in range(quantidade):

    print()

    produto = input("Produto: ")
    preco = float(input("Preço: "))
    qtd = int(input("Quantidade: "))

    produtos.append(produto)
    precos.append(preco)
    quantidades.append(qtd)

print()
print("CUPOM FISCAL")
print("=" * 50)

total = 0

for i in range(len(produtos)):

    subtotal = precos[i] * quantidades[i]

    print(produtos[i])
    print("Subtotal:", subtotal)

    total = subtotal

print("=" * 50)

if total >= 200:
    desconto = total * 0.1
else:
    desconto = 0

print("Desconto:", desconto)
print("Total:", total - desconto)