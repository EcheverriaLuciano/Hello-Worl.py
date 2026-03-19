# 3) Monitor de Inundação (Sentinela)

while True:
    nivel_rio = float(input("Digite o nível do rio (em metros): "))

    if nivel_rio < 0:
        print(" Valor Invalido. \nLeitura encerrada.")
        break
    elif nivel_rio < 3:
        print("Estado Normal")
    elif nivel_rio <= 5:
        print("Estado de Alerta")
    else:
        print("Evacuação Imediata")
