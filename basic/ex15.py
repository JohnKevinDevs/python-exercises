aluno = {
    "NOME": "JOHN KEVIN",
    "IDADE": "17",
    "CURSO": "SIT"
}

chave = input("Chave atualizada: ").upper()
att_co = input("Valor atualizado: ").upper()

if chave in aluno:
    aluno[chave] = att_co
else:
    print(f"A chave {chave} não existe no dicionário")

add_ch = input("Chave adicionada: ").upper()
add_co = input("Valor da chave: ").upper()

aluno[add_ch] = add_co

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")