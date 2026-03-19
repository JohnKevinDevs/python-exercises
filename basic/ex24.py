def converter_temperatura(temp, escala_inicial, escala_final):
    if escala_inicial == "C":
        celsius = temp
    elif escala_inicial == "F":
        celsius = (temp-32) * 5/9
    elif escala_inicial == "K":
        celsius = temp - 273
    else:
        return None
    
    if escala_final == "C":
        return celsius
    elif escala_final == "F":
        return (celsius * 9/5) + 32
    elif escala_final == "K":
        return celsius + 273
    else:
        return None

temp = float(input("Digite a temperatura: "))
escala_inicial = input("Digite a escala inicial: ").upper
escala_final = input("Digite a escala final: ").upper

resultado = converter_temperatura(temp, escala_inicial, escala_final)

if escala_final is not None:
    print(f"{temp:.2f}º {escala_inicial} = {resultado:.2f}º {escala_final}")
else:
    print("Escala Inválida, use C, F ou K")