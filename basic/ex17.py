loja = [
    {"NOME": "BANANA", "PREÇO": "5", "QTD": "12"},
    {"NOME": "MAÇA", "PREÇO": "10", "QTD": "6"},
    {"NOME": "MARACUJÁ", "PREÇO": "15", "QTD": "24"}
]

t = 0

for fruta in loja:
    t+=1
    print(f"{t}º FRUTA -> NOME: {fruta['NOME']}; PREÇO: {fruta['PREÇO']}; QTD: {fruta['QTD']}")

while t != 0:
    op = int(input("Digite o número da fruta: "))
    cont = input("Digite o conteúdo que deseja ver: ").upper()

    print(f"O {cont} da {op}ª fruta é: {loja[op-1][cont]}")

    t = int(input("Se deseja parar de acessar os conteúdos, digite 0: "))