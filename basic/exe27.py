def media_final(n1, n2, n3):
    media = (n1 + n2 + n3)/4
    return media



n1 = float(input("Digite sua nota"))
n2 = float(input("Digite sua nota"))
n3 = float(input("Digite sua nota"))

final = media_final(n1, n2, n3)

if final>=7:
    print("Aprovado")
elif final >=5 and final <= 6.9:
    print("Recuperação")
else:
    print("reprovado") 

