import json


ficheiro = "ficheirosTEstes/dados.txt"


with open(ficheiro, "r") as f:
    conteudo = f.read()


print(conteudo)

nomes = "ficheirosTEstes/nomes.txt"

with open(nomes, "w") as fi:
    fi.write("Ponto\n")
    fi.write("Tiago\n")


nomesJSon = "ficheirosTEstes/nomes.json"
with open(nomesJSon, "r") as f:
    dados = json.load(f)

print(dados)


nome = {"nome": "Balls", "idade": 67}

dados.append(nome)

with open(nomesJSon, "w") as f:
    json.dump(dados, f, indent=4)