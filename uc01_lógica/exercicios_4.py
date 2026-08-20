print("=" * 50)
print("LOJA")
print("=" * 50)

quantidade = int(input("Quantos produtos deseja comprar? "))

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
print("=" * 50)
print("RESUMO DA COMPRA")
print("=" * 50)

total = 0
maior = 0
produto_caro = ""

for i in range(len(produtos)):

    subtotal = precos[i] * quantidades[i]

    print(produtos[i])
    print("Preço:", precos[i])
    print("Quantidade:", quantidades[i])
    print("Subtotal:", subtotal)
    print()

    total = subtotal

    if precos[i] > maior:
        maior = precos[i]

    produto_caro = produtos[i]

if total >= 500:
    desconto = total * 0.15
else:
    desconto = 0

print("=" * 50)
print("Produto mais caro:", produto_caro)
print("Preço:", maior)
print("Desconto:", desconto)
print("Valor Final:", total - desconto)