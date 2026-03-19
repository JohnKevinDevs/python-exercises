import math

A = int(input("Digite o número de início: "))
B = int(input("Digite o número de fim: "))

for num in range(A, B+1):

    raiz_quadrada = False

    raiz_cubica = False

    x = math.sqrt(num)

    y = math.pow(num, 1/3)

    y = round(y)

    if x.is_integer():

        raiz_quadrada = True

    if isinstance(y, int):

        raiz_cubica = True

    if raiz_quadrada and raiz_cubica:

        print(f"O número {num} é raiz quadrada e cúbica de números inteiros: {x:.0f}² e {y}³")