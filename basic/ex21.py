def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in palavra if letra in vogais)

def exibir_contagem_vogais(lista_palavras):
    for palavra in lista_palavras:
        contagem = contar_vogais(palavra)
        print(f"A palavra '{palavra}' tem {contagem} vogais.")

def main():
    
    entrada = input("Digite uma lista de palavras separadas por espaço: ")
    lista_palavras = entrada.split()
    
    exibir_contagem_vogais(lista_palavras)

main()
