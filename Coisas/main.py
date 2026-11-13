from funcoes import criar_jogador, criar_inimigos, contar_vivos
from funcoes import mostrar_menu, atacar, mostrar_estado
from funcoes import listar_inimigos, usar_pocao

print("=== BATALHA DE INIMIGOS ===")

jogador = criar_jogador()
inimigos = criar_inimigos()
print("Apareceram", len(inimigos), "inimigos!")

resultado = ""

while resultado == "":
    mostrar_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        atacar(jogador, inimigos)
    elif opcao == "2":
        mostrar_estado(jogador, inimigos)
    elif opcao == "3":
        listar_inimigos(inimigos)
    elif opcao == "4":
        usar_pocao(jogador)
    elif opcao == "5":
        resultado = "FUGA"
    else:
        print("Opção inválida!")

    # verificar se o jogo acabou
    if resultado == "":
        if jogador["vida"] <= 0:
            resultado = "DERROTA"
        elif contar_vivos(inimigos) == 0:
            resultado = "VITORIA"

print()
if resultado == "VITORIA":
    print("VITÓRIA! Derrotaste todos os inimigos!")
elif resultado == "DERROTA":
    print("DERROTA! Ficaste sem vida.")
else:
    print("Partida terminada por FUGA.")

print("Pontuação final:", jogador["pontos"])