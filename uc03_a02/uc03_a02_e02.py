categorias = ["Tênis", "Sandália", "Chinelo", "Bota"]

nome = input("Nome do produto: ")
categoria = input("Categoria: ")
preco = float(input("Preço: "))
estoque = int(input("Quantidade em estoque: "))
tamanho = int(input("Tamanho: "))

if len(nome) < 3:
    print("ERRO: Nome inválido")
elif categoria not in categorias:
    print("ERRO: Categoria inválida")
elif preco <= 0:
    print("ERRO: Preço inválido")
elif estoque < 0:
    print("ERRO: Estoque inválido")
elif tamanho <= 0:
    print("ERRO: Tamanho inválido")
else:
    print("\nPRODUTO CADASTRADO COM SUCESSO!")
    print(f"Produto: {nome}")
    print(f"Categoria: {categoria}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque}")
    print(f"Tamanho: {tamanho}")

    if preco >= 500:
        classificacao = "Produto Premium"
    elif preco >= 300:
        classificacao = "Produto Intermediário"
    else:
        classificacao = "Produto Econômico"

    print(f"Classificação: {classificacao}")

    if estoque <= 5:
        print("Status do estoque: ESTOQUE BAIXO")
    else:
        print("Status do estoque: ESTOQUE NORMAL")