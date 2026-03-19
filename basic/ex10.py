print("Bem vindo ao Banco JK")
op = 1
saldo = 0
depositos = 0

while op != 0:
    saldo += float(input("Valor do Depósito: "))
    depositos += 1
    op = int(input("Se deseja parar digite 0: "))

media = saldo/depositos

print(f"Quantia depositada: R${saldo:.2f}")
print(f"Média dos depósitos: R${media:.2f}")