meses = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
         'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')

mes = input("Digite o mês: ").upper()

posicao = meses.index(mes)

print(f"{mes} é o {posicao+1}º mês do ano")