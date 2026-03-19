def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Digite o número: "))
resultado = fibonacci(n-1)

print(f"Fibonacci de {n} = {resultado}")