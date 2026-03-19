def num_maior(lista_numeros):
    crescente = sorted(lista_numeros)
    maior = crescente[2]
    return maior

numeros = input("Digite 3 números, dividindo-os por ',': ")
lista_numeros = [float(num) for num in numeros.split(",")]

maior = num_maior(lista_numeros)
print(f"O maior número é: {maior:.2f}")