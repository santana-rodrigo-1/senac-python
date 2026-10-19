"""
Crie uma lista com 5 nomes e exiba todos com for.
Adicione e remova elementos dessa lista; mostre o tamanho.
Crie uma tupla com 3 cidades e acesse a primeira.
Crie um dicionário representando um aluno (nome, idade, curso).
Percorra o dicionário exibindo chave e valor com .items().
"""

nomes = ["nome01", "nome02", "nome03", "nome04", "nome05"]

for nome in nomes:
    print(nome)

print(f"TOTAL DE NOMES: {len(nomes)}\n")

nomes.append("nome006")  # adiciona no fim​
nomes.remove("nome02")  # remove pelo valor​

for nome in nomes:
    print(nome)

print(f"TOTAL DE NOMES: {len(nomes)}\n")

cidades = ("RJ", "SP", "BA")

for cidade in cidades:
    print(cidade)

print(f"TOTAL DE CIDADES: {len(cidades)}\n")

print(f"A PRIMEIRA CIDADE LISTADA É: {cidades[0]}")

aluno = {"nome": "Ana", "idade": 20, "curso": "Python"}
print(aluno["nome"])  # Ana  (acesso pela CHAVE)​
