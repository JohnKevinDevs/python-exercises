import random
import math



def randomLista(qtd):
    cont = 0
    lista = []    
    while cont < qtd:

        sorteado = random.randint(1,100)       
        while sorteado in lista:
            sorteado = random.randint(1,100) 
        else:
            lista.append(sorteado)
        cont += 1
    return sorted(lista)


listaNum = randomLista(10)





def buscaBinaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    tentativas = 0

    while inicio <= fim:
        tentativas += 1
        meio = (inicio + fim) // 2  
        if lista[meio] == valor:
            return (tentativas, meio) 
        elif valor < lista[meio]:
            fim = meio - 1 
        else:
            inicio = meio + 1  

    return (tentativas, -1)  




print("Lista gerada:", listaNum)


Busca = int(input("Digite o valor que deseja buscar: "))

tentativas, indice = buscaBinaria(listaNum, Busca)

if indice != -1:
    print(f"Valor {Busca} encontrado na posição {indice} em {tentativas} tentativas.")