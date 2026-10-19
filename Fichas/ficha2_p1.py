
lista = []

respostaWhile = "S"

respostaLista = 0

adiciona = ""

while respostaWhile == "S":
    print("Oque pretendes fazer: ")
    print("   Adicionar uma tarefa - 1")
    print("   Adicionar várias tarefa - 2")
    print("   Adicionar uma tarefa em uma posicao especifica - 3")
    print("   Remover tarefa por nome - 4")
    print("   Remover ultima tarefa ou por uma posicao especifica - 5")
    print("   Remover todas as tarefas - 6")
    print("   Ver quantas vezes aparece uma certa tarefa - 7")
    print("   Ver a primeira tarefa da lista - 8")
    print("   Ordenar as tarefas por ordem alfabetica - 9")
    print("   Inverter a ordem das tarefas - 10")
    print("   Criar uma copia da lista de tarefas - 11")
    print("   Sair do menu - 0")
    resposta = int(input("Escreve a opcao que pretende executar(1,2,3,....)"))
    
    if(resposta == 0):
        respostaWhile="N"
        
    elif(resposta == 1):
        adiciona = input("Adicionar uma tarefa: ") 
        lista.append(adiciona)
        adiciona= ""
        
    elif(resposta == 2):
        adiciona = input("Adiciona tarefas: ")
        lista.extend(adiciona.split(','))
        
    elif(resposta == 3):
        adiciona = input("Adiciona uma tarefa : ")
        adiciona = input("Que posicao a queres uma tarefa : ")
        lista.extend(adiciona.split(','))
        
        
        
print(lista)

