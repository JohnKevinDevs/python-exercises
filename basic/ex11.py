print("Crie uma senha")
print("*Min: 8 Caracteres / 1 Letra Maiúscula / 1 Letra Minúscula / 1 Número")
senha = str(input("Digite a senha: "))
maiuscula = False
minuscula = False
numero = False

for caractere in senha:
    if caractere.isdigit():
        numero = True
    if caractere.isupper():
        maiuscula = True
    if caractere.islower():
        minuscula = True

if len(senha) >= 8 and maiuscula and minuscula and numero:
    print("Senha feita com sucesso")
else:
    print("Senha Inválida")
    if len(senha) < 8:
        print("Senha muito curta (Mínimo: 8 Caracteres)")
    if not maiuscula:
        print("Não tem letra maiúscula")
    if not minuscula:
        print("Não tem letra minúscula")
    if not numero:
        print("Não tem número")