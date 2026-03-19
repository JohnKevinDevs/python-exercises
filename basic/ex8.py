print("Tabela de Turnos:")
print("1 - Manhã")
pag_manha = 15
print("2 - Tarde")
pag_tarde = 18
print("3 - Noite")
pag_noite = 25

turno = int(input("Qual o seu turno: "))
horas = float(input("Horas trabalhadas: "))

if turno == 1:
    salario = horas * pag_manha
    print(f"Seu salário diurno é: R${salario:.2f}")
elif turno == 2:
    salario = horas * pag_tarde
    print(f"Seu salário vespertino é: R${salario:.2f}")
elif turno == 3:
    salario = horas * pag_noite
    print(f"Seu salário noturno é: R${salario:.2f}")
else:
    print("Opção Inválida")