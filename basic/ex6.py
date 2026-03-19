idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print(f"Você tem {idade} anos e é uma criança")
elif 13 <= idade <= 17:
    print(f"Você tem {idade} anos e é um adolescente")
elif 18 <= idade <= 60:
    print(f"Você tem {idade} anos e é um adulto")
else:
    print(f"Você tem {idade} anos e é um idoso")