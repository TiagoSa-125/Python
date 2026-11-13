import random

def menu():
    print("------Batalha------")
    print("1 - Atacar inimigo")
    print("2 - Consultar estado do jogador") 
    print("2 - Listar inimigos vivos") 
    print("2 - Usar poção de cura") 
    print("2 - Fugir / terminar jogo") 
    opcao = input("Escolha uma opção: ")
    
    return opcao
    

def escolheInimigo(inimigos):
    quantidade = random.randint(3, 5)
    print("Quantidade de inimigos: ", quantidade)
    inimigosSelecionados = []
    
    for i in range(quantidade):
        inimigosSelecionados.append(random.choice(inimigos))
        
    return inimigosSelecionados

def atacarInimigo(inimigosSelecionados, ):
    ...