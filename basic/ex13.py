tanque = 50
l_volta = 5
voltas = 0
total_voltas = 20

print("SIMULADOR DE CORRIDA JK!")

while voltas < total_voltas:
    if tanque >= l_volta:
        voltas += 1
        tanque -= l_volta
        print(f"{voltas} ª VOLTA: COMBUSTÍVEL: {tanque} LITROS ")
    elif tanque <= l_volta:
        print("TANQUE BAIXO! REABASTEÇA!")
        tanque = (total_voltas - voltas) * l_volta
        print(f"REABASTECIDO: COMBUSTÍVEL: {tanque} LITROS")

print("Fim da simulação da corrida")
print(f"Você deu {voltas} voltas")