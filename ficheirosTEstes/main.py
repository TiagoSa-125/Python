ficheiro = "ficheirosTEstes/dados.txt"


with open(ficheiro, "r") as f:
    conteudo = f.read()


print(conteudo)

nomes = "ficheirosTEstes/nomes.txt"

with open(nomes, "w") as fi:
    fi.write("Ponto\n")
    fi.write("Tiago\n")


