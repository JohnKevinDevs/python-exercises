produtos = []
qtd_produtos = []
op = 4
print("Bem Vindo ao Estoque JK")
print("MENU")
print("0 - SAIR")
print("1 - COMPRAR")
print("2 - VENDER")

while op != 0:
    op = int(input("Opção Desejada: "))
    if op == 1:
        print("COMPRAS")
        produto = str(input("Produto Comprado: ")).upper()
        if produto in produtos:
            pos = produtos.index(produto)
            qtd = int(input("Quantidade Comprada: "))
            if qtd <= 0:
                print("Quantidade Inválida! Digite um número maior que 0")
            else:
                qtd_produtos[pos] += qtd
                print("ESTOQUE DE PRODUTOS")
                for p, q in zip(produtos, qtd_produtos):
                    print(f"{p}: {q} unidades")
        else:
            produtos.append(produto)
            qtd = int(input("Quantidade Comprada: "))
            if qtd <= 0:
                print("Quantidade Inválida! Digite um número maior que 0")
            else:
                qtd_produtos.append(qtd)
                print("ESTOQUE DE PRODUTOS")
                for p, q in zip(produtos, qtd_produtos):
                    print(f"{p}: {q} unidades")
    elif op == 2:
        if not produtos:
            print("Não há produtos para serem vendidos")
        else:
            print("VENDAS")
            produto = str(input("Produto Vendido: ")).upper()
            if produto not in produtos:
                print("Esse produto não está no estoque")
            else:
                pos = produtos.index(produto)
                venda = int(input("Quantidade Vendida: "))
                if venda <= 0:
                    print("Quantidade Inválida")
                elif venda > qtd_produtos[pos]:
                    print("Estoque Insuficiente")
                else:
                    qtd_produtos[pos] -= venda
                    if qtd_produtos[pos] == 0:
                        produtos.pop(pos)
                        qtd_produtos.pop(pos)
                    print("ESTOQUE DE PRODUTOS")
                    if not produtos:
                        print("Estoque Vazio")
                    else:
                        for p, q in zip(produtos, qtd_produtos):
                            print(f"{p}: {q} unidades")
    elif op == 0:
        print("Programa Encerrado")
        print("ESTOQUE DE PRODUTOS FINAL")
        if not produtos:
            print("Estoque Vazio")
        else:
            for p, q in zip(produtos, qtd_produtos):
                print(f"{p}: {q} unidades")
    else:
        print("Opção Inválida")