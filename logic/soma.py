def soma(n):
    if n == 0:
        return 0
    else:
        return n + soma(n-1)
    
n = int(input("Digite o número: "))
resultado = soma(n)

print(f"Soma de 1 a {n}: {resultado}")