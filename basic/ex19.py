caracter = input("Digite o Caracter desejado: ")

def quadrado(caracter):
    print("QUADRADO: \n")
    print(caracter*5)
    for x in range(2):
        print(f"{caracter}   {caracter}")
    print(caracter*5)

def retangulo(caracter):
    print("RETÂNGULO: \n")
    print(caracter*7)
    for x in range(4):
        print(f"{caracter}     {caracter}")
    print(caracter*7)

def triangulo(caracter):
    print("TRIÂNGULO: \n")
    print(f"  {caracter}")
    print(f" {caracter} {caracter}")
    print(f"{caracter} {caracter} {caracter}")

quadrado(caracter)
print("\n")
retangulo(caracter)
print("\n")
triangulo(caracter)
print("\n")