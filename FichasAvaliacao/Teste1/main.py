from functions import escolheInimigo, atacarInimigo, menu


Jogador = {"Vida": 300, "Ataque": 20, "Pocoes": 2, "Pontos":0}

Inimigos = [
    {"nome": "Goblin", "Vida": 40, "Ataque": 8, "Pontos": 100},
    {"nome": "Orc", "Vida": 55, "Ataque": 11, "Pontos": 200},
    {"nome": "Troll", "Vida": 70, "Ataque": 14, "Pontos": 300},
    {"nome": "Beast", "Vida": 85, "Ataque": 17, "Pontos": 400},
    {"nome": "Dragao", "Vida": 100, "Ataque": 20, "Pontos": 500},
]

escolha = menu()

inimigosSelecionados = escolheInimigo(Inimigos)


# while True:
#     match(escolha):
#         case "1":
#             ...