import math

def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_desvio_padrao(lista):
    media = calcular_media(lista)
    soma_quadrados = sum([(x - media) ** 2 for x in lista])
    return math.sqrt(soma_quadrados / len(lista))

def classificar_lista(lista):
    return sorted(lista)

def main():
    
    entrada = input("Digite uma lista de números separados por vírgula: ")
    lista_numeros = [float(num) for num in entrada.split(',')]
    
    media = calcular_media(lista_numeros)
    desvio_padrao = calcular_desvio_padrao(lista_numeros)
    lista_ordenada = classificar_lista(lista_numeros)
    
    print(f"Média: {media:.2f}")
    print(f"Desvio padrão: {desvio_padrao:.2f}")
    print(f"Lista ordenada: {lista_ordenada}")

main()
