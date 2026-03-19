# 4) O Coletor de Itens e Inventário

capacidade_maxima = 15.0
peso_total = 0.0

while peso_total <= capacidade_maxima:
    peso_item = float(input("Digite o peso do item (kg): "))

    if peso_total + peso_item > capacidade_maxima:
        print("Mochila cheia, item descartado.")
        break

    peso_total += peso_item
    print(f"Item adicionado. Peso atual da mochila: {peso_total:.2f} kg")

print(f"Peso final total na mochila: {peso_total:.2f} kg")
