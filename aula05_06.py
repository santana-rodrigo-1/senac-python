# Compra Liberada (not)
# O cliente só poderá finalizar a compra se não estiver inadimplente.
# not inadimplente

inadimplente = (input("O cliente esta inadimplente ? (s/m) "))

if not inadimplente == "s":
    print("compra autorizada.")
else:
    print("Compra não autorizada.")
