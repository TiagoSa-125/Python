from functions import consultarEstado, escolheInimigo, atacarInimigo, listarInimigosVivos, menu, usarPocao


Jogador = {"Vida": 300, "Ataque": 20, "Pocoes": 2, "Pontos":0,"Inimigos": 0}

Inimigos = [
    {"nome": "Goblin", "Vida": 40, "Ataque": 8, "Pontos": 100, },
    {"nome": "Orc", "Vida": 55, "Ataque": 11, "Pontos": 200},
    {"nome": "Troll", "Vida": 70, "Ataque": 14, "Pontos": 300},
    {"nome": "Beast", "Vida": 85, "Ataque": 17, "Pontos": 400},
    {"nome": "Dragao", "Vida": 100, "Ataque": 20, "Pontos": 500},
]

escolha = menu()

inimigosSelecionados = escolheInimigo(Inimigos)

estado = ""
while estado == "":
    if(escolha >= "1" and escolha <= "5"):
        match(escolha):
            case "1":
                atacarInimigo(inimigosSelecionados, Jogador)
                
            case "2":
                consultarEstado(Jogador, inimigosSelecionados)
            case "3":
                listarInimigosVivos(inimigosSelecionados)
            case "4":
                usarPocao(Jogador)
            case "5":
                print("Fugiste do jogo ficaste com ",Jogador["Pontos"], " pontos")
                estado = "FUGA"
                break
    else:
        print("Escolha inválida")
        
    if Jogador["Vida"] <= 0:
        print("Perdeste o jogo :( ficaste com ",Jogador["Pontos"], " pontos")
        estado = "DERROTA"
        break
    if len(inimigosSelecionados) == 0:
        print("Venceste o jogo PARABENS :) ficaste com ",Jogador["Pontos"], " pontos")
        estado = "VITORIA"
        break
    escolha = menu()
