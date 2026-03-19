def eh_palindromo(palavra):
    if palavra == palavra[::-1]:
        palindromo = True
    else:
        palindromo = False
    return palindromo

palavra = input("Digite a palavra: ")
palindromo = eh_palindromo(palavra)

if palindromo == True:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")