import random

def menu():
    print("\n------Batalha------")
    print("1 - Atacar inimigo")
    print("2 - Consultar estado do jogador") 
    print("3 - Listar inimigos vivos") 
    print("4 - Usar poção de cura") 
    print("5 - Fugir / terminar jogo") 
    opcao = input("Escolha uma opção: ")
    
    return opcao
    

def escolheInimigo(inimigos):
    quantidade = random.randint(3, 5)
    print("Quantidade de inimigos: ", quantidade)
    inimigosSelecionados = []
    
    for i in range(quantidade):
        inimigosSelecionados.append(random.choice(inimigos))
        inimigos.remove(inimigosSelecionados[i])
        
    return inimigosSelecionados

def atacarInimigo(inimigosSelecionados, Jogador):    
    if len(inimigosSelecionados) == 0:
        print("Não existem inimigos vivos.")
        return
    
    print("Qual Inimigo queres atacar:")
    
    for i in range(len(inimigosSelecionados)):
        if(inimigosSelecionados[i]["Vida"] > 0):
            print(i+1, "-", inimigosSelecionados[i]["nome"])
    
    
    inimgoEscolhido = int(input("Escolha um inimigo: ")) - 1
    
    if inimgoEscolhido < 0 or inimgoEscolhido >= len(inimigosSelecionados):
        print("Inimigo inválido")
        return
    
    danoJogador = random.randint(10,20)
    danoInimigo = random.randint(5,inimigosSelecionados[inimgoEscolhido]["Ataque"])
    
    inimigosSelecionados[inimgoEscolhido]["Vida"] -= danoJogador
    print("Causaste: ", danoJogador, " de dano ao inimigo ", inimigosSelecionados[inimgoEscolhido]["nome"])
    
    if inimigosSelecionados[inimgoEscolhido]["Vida"] <= 0 :
        print("Inimigo ", inimigosSelecionados[inimgoEscolhido]["nome"], " foi derrotado!")
        Jogador["Pontos"] += inimigosSelecionados[inimgoEscolhido]["Pontos"]
        print("Ganhaste ", inimigosSelecionados[inimgoEscolhido]["Pontos"], " pontos")
        Jogador["Inimigos"] += 1
        inimigosSelecionados.pop(inimgoEscolhido)
    else:
        print("O inimigo ", inimigosSelecionados[inimgoEscolhido]["nome"], " ainda está vivo com ", inimigosSelecionados[inimgoEscolhido]["Vida"], " de vida e vai contra-atacar")
        Jogador["Vida"] -= danoInimigo
        print("Recebeste: ", danoInimigo, " de dano do inimigo ", inimigosSelecionados[inimgoEscolhido]["nome"], " ficaste com ", Jogador["Vida"], " de vida")
   
    # if len(inimigosSelecionados) == 0:
    #     return
    

def consultarEstado(Jogador, inimigosSelecionados):
    print("\nEstado do jogador:")
    print("Vida: ", Jogador["Vida"])
    print("Poções: ", Jogador["Pocoes"])
    print("Pontos: ", Jogador["Pontos"])
    print("Inimigos derrotados: ", Jogador["Inimigos"])
    print("Ainda tens ", len(inimigosSelecionados), " inimigos vivos")

def listarInimigosVivos(inimigosSelecionados):
    print("\nInimigos vivos:")
    for i in range(len(inimigosSelecionados)):
        if(inimigosSelecionados[i]["Vida"] > 0):
            print(i+1, "-", inimigosSelecionados[i]["nome"], " com ", inimigosSelecionados[i]["Vida"], " de vida", " e ", inimigosSelecionados[i]["Ataque"], " de ataque")
            
def usarPocao(Jogador):    
    if Jogador["Pocoes"] > 0:
        if Jogador["Vida"] < 100:
            cura = 25
            Jogador["Vida"] += cura
            Jogador["Pocoes"] -= 1
            print("Usaste uma poção de cura e recuperaste ", cura, " de vida ficaste com ", Jogador["Vida"], " de vida e ainda tens ", Jogador["Pocoes"], " poções")
        else:
            print("\nSó podes usar uma poção de cura se tiveres menos de 100 de vida")
    else:
        print("Não tens poções de cura disponíveis")
        