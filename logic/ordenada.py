import random

# Função que cria uma lista aleatória sem repetição
def randomLista(qtd):
    cont = 0
    lista = []    
    while cont < qtd:
        sorteado = random.randint(1,100)       
        while sorteado in lista:
            sorteado = random.randint(1,100) 
        lista.append(sorteado)
        cont += 1
    return lista

listaRandom = randomLista(10)
print(f"A lista aleatória é: {listaRandom}")

def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

listaOrdenada = selection_sort(listaRandom)
print(f"Lista Ordenada: {listaOrdenada}")