# Abrir um arquivo - open() e seus modos

with open("dados.txt", "w", encoding="uft-8") as f:
    f.write("Ana\n")
# o 'with' fecha o arquivo sozinho ao terminar.

