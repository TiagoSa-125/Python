import random

vida_maxima = 300
cura_pocao = 25

tipos_inimigo = [
    {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    {"nome": "Dragão", "vida": 100, "ataque": 20, "pontos": 500},
]


def criar_jogador():
    
    return  {
            "vida": 300, "ataque": 20, "pocoes": 2, "pontos": 0, "derrotados": 0,
        }


def criar_inimigos():
    quantidade = random.randint(3, 5)
    inimigos = []
    for i in range(quantidade):
        modelo = random.choice(tipos_inimigo)
        inimigos.append(modelo.copy())
    return inimigos


def contar_vivos(inimigos):
    total = 0
    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            total = total + 1
    return total


def mostrar_menu():
    print()
    print("========== BATALHA ==========")
    print("1 — Atacar inimigo")
    print("2 — Consultar estado do jogador")
    print("3 — Listar inimigos vivos")
    print("4 — Usar poção de cura")
    print("5 — Fugir / terminar jogo")


def listar_inimigos(inimigos):
    if contar_vivos(inimigos) == 0:
        print("Não existem inimigos vivos.")
        return

    numero = 1
    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            print(numero, "-", inimigo["nome"], "| Vida:", inimigo["vida"], "| Ataque:", inimigo["ataque"])
            numero = numero + 1


def atacar(jogador, inimigos):
    # lista só com os inimigos vivos
    vivos = []
    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            vivos.append(inimigo)

    if len(vivos) == 0:
        print("Não há inimigos para atacar.")
        return

    listar_inimigos(inimigos)
    escolha = input("Escolhe o inimigo: ")

    # isdigit() verifica se o texto é um número (evita erros)
    if not escolha.isdigit():
        print("Tens de escrever um número!")
        return

    escolha = int(escolha)
    if escolha < 1 or escolha > len(vivos):
        print("Número fora do intervalo!")
        return

    inimigo = vivos[escolha - 1]

    # ataque do jogador
    dano = random.randint(10, 20)
    inimigo["vida"] = inimigo["vida"] - dano
    if inimigo["vida"] < 0:
        inimigo["vida"] = 0
    print("Causaste", dano, "de dano ao", inimigo["nome"])

    if inimigo["vida"] == 0:
        print("Derrotaste o", inimigo["nome"], "!")
        jogador["pontos"] = jogador["pontos"] + inimigo["pontos"]
        jogador["derrotados"] = jogador["derrotados"] + 1
    else:
        # contra-ataque do inimigo
        dano_inimigo = random.randint(5, inimigo["ataque"])
        jogador["vida"] = jogador["vida"] - dano_inimigo
        if jogador["vida"] < 0:
            jogador["vida"] = 0
        print("O", inimigo["nome"], "contra-atacou e causou", dano_inimigo, "de dano")


def mostrar_estado(jogador, inimigos):
    print("Vida:", jogador["vida"])
    print("Pontuação:", jogador["pontos"])
    print("Inimigos derrotados:", jogador["derrotados"])
    print("Inimigos vivos:", contar_vivos(inimigos))
    print("Poções:", jogador["pocoes"])


def usar_pocao(jogador):
    if jogador["pocoes"] == 0:
        print("Não tens poções!")
    elif jogador["vida"] >= vida_maxima:
        print("Já tens a vida cheia!")
    else:
        jogador["vida"] = jogador["vida"] + cura_pocao
        if jogador["vida"] > vida_maxima:
            jogador["vida"] = vida_maxima
        jogador["pocoes"] = jogador["pocoes"] - 1
        print("Usaste uma poção. Vida:", jogador["vida"])