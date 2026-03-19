def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
n = int(input("Digite o número: "))
resultado = fatorial(n)

print(f"{n}! = {resultado}")