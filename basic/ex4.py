n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))

if n1 > n2:
    print(f"O 1º número ({n1}) é maior")
elif n1 < n2:
    print(f"O 2º número ({n2}) é maior")
else:
    print("Os números são iguais")