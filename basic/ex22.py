print("CALCULADORA JK")
print("1 - SOMAR")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")
print("0 - SAIR")

def soma(n1, n2):
    resultado = n1+n2
    print(f"Resultado: {resultado}")
def sub(n1, n2):
    resultado = n1-n2
    print(f"Resultado: {resultado}")
def mult(n1, n2):
    resultado = n1*n2
    print(f"Resultado: {resultado}")
def div(n1, n2):
    if n2 == 0:
        print("ERRO! IMPOSSÍVEL DIVIDIR POR 0")
    else:
        resultado = n1/n2
        print(f"Resultado: {resultado}")

def calc(op):
    if (op == 1):
        soma(n1, n2)
    elif (op == 2):
        sub(n1, n2)
    elif (op == 3):
        mult(n1, n2)
    elif (op == 4):
        div(n1, n2)
    else:
        print("OPÇÃO INVÁLIDA")

while True:

    op = int(input(("OPÇÃO DESEJADA: ")))
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))

    if (op==0):
        print("SAINDO DO SISTEMA")
        break

    calc(op)