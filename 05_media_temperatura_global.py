# 5) Média de Temperatura Global

quantidade_dias = int(input("Quantos dias deseja analisar? "))

soma_temperaturas = 0.0
contador = 0

while contador < quantidade_dias:
    temp = float(input(f"Digite a temperatura do dia {contador + 1}: "))
    soma_temperaturas += temp
    contador += 1

media = soma_temperaturas / quantidade_dias
print(f"\nMédia das temperaturas: {media:.2f}°C")

if media > 25:
    print("Acima do esperado")
else:
    print("Dentro da normalidade")
