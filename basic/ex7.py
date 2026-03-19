print("Tabela do Pedágio:")
print("1 - Moto")
pag_moto = 3
print("2 - Carro")
pag_carro = 7
print("3 - Caminhão")
pag_caminhao = 12

op = int(input("Qual o seu veículo: "))

if op == 1:
    print(f"O pedágio da moto é: R${pag_moto:.2f}")
elif op == 2:
    print(f"O pedágio do carro é: R${pag_carro:.2f}")
elif op == 3:
    print(f"O pedágio do caminhão é: R${pag_caminhao:.2f}")
else:
    print("Opção Inválida")