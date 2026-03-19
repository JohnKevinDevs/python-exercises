def calcular_desconto(preco_inicial, percentual):
    desconto = preco_inicial * (percentual / 100)
    preco_final = preco_inicial - desconto
    return preco_final

preco_inicial = float(input("Digite o preço inicial: "))
percentual = float(input("Digite o percentual de desconto: "))

preco_final = calcular_desconto(preco_inicial, percentual)
print(f"Preço Final: R$ {preco_final}")