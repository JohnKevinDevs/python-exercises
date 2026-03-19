A = int(input("Digite o número de início: "))
B = int(input("Digite o número de fim: "))
S = int(input("Digite o número de soma: "))

for num in range(A, B+1):

    algarismos = list(str(num))

    algarismos = [int(n) for n in str(num)]

    soma = 0

    for algarismo in algarismos:

        soma += algarismo

    if soma == S:

        print(f"Numero presente no intervalo de {A} a {B} que a soma de dígitos é equivalente a {S}: {num}")