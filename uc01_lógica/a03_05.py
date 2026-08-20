# Custo de Viagem.
# Calcule quntos litros serão necessários e o custo total da viagem.
# (distancia / consumo) * preço

distancia = float(input("\n\nDigite a distância em Km: "))
consumo = float(input("Digite o consumo de combustível: "))
preco = float(input("Digite o preço do combustível: "))

custo = (distancia / consumo) * preco

print(f"Distância: {distancia}")
print(f"Consumo: {consumo}")
print(f"Preço: {preco}")
print(f"O custo da viagen sera de: {custo}")
