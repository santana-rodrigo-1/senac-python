total = 0 ; qtd = 0

while True:
    e = input("Preço (ou fim): ")
    if e.lower() == "fim":
        break
    total += float(e)
    qtd += 1
print(f"Itens: {qtd}")
print(f"Total: R$ {total:.2f}")
