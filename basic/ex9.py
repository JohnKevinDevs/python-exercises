op = 0
andar_atual = 0
andar_futuro = 0

print("Bem vindo ao elevador")
print("Opções:")
print("1 - Subir")
print("2 - Descer")
print("3 - Parar")

while op != 3:
    print(f"Você está no {andar_atual}º andar")
    op = int(input("Opção Desejada: "))
    if op == 1:
        andar_futuro = int(input("Qual andar você deseja ir: "))
        if 0 <= andar_futuro <= 10 and andar_atual < andar_futuro:
            andar_atual = andar_futuro
        elif andar_futuro < 0 or andar_futuro > 10:
            print("Andar inexistente")
        else:
            print("Andar Inválido")
    elif op == 2:
        andar_futuro = int(input("Qual andar você deseja ir: "))
        if 0 <= andar_futuro <= 10 and andar_atual > andar_futuro:
            andar_atual = andar_futuro
        elif andar_futuro < 0 or andar_futuro > 10:
            print("Andar inexistente")
        else:
            print("Andar Inválido")
    elif op == 3:
        print(f"Você parou no {andar_atual}º andar")
    else:
        print("Opção Inválida")