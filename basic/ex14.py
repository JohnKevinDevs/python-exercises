filmes = ["VELOZES E FURIOSOS", "BATMAN", "CORINGA", "MISSÃO IMPOSSÍVEL", "SUPERMAN"]

for filme in filmes:
    print(filme)

filme_add = input("Adicione um novo filme: ").upper()
filmes.append(filme_add)

filme_rem = input("Remova um filme: ").upper()
filmes.remove(filme_rem)

for filme in filmes:
    print(filme)