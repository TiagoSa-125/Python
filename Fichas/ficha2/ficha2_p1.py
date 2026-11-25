
lista = []

respostaWhile = "S"

respostaLista = 0

respostaifs = ""

while respostaWhile == "S":
    print("\n\nOque pretendes fazer: ")
    print("   Adicionar uma tarefa - 1")
    print("   Adicionar várias tarefa - 2")
    print("   Adicionar uma tarefa em uma posicao especifica - 3")
    print("   Remover tarefa pelo nome dela - 4")
    print("   Remover ultima tarefa ou por uma posicao especifica - 5")
    print("   Remover todas as tarefas - 6")
    print("   Ver quantas vezes aparece uma certa tarefa - 7")
    print("   Ver a primeira tarefa da lista - 8")
    print("   Ordenar as tarefas por ordem alfabetica - 9")
    print("   Inverter a ordem das tarefas - 10")
    print("   Criar uma copia da lista de tarefas - 11")
    print("   Sair do menu - 0")
    resposta = int(input("\nEscreve a opcao que pretende executar(1,2,3,....)"))
    
    if(resposta == 0):
        respostaWhile="N"
        
    elif(resposta == 1):
        respostaifs = input("\n\nAdicionar uma tarefa: ") 
        lista.append(respostaifs)
        
    elif(resposta == 2):
        respostaifs = input("\n\nAdiciona tarefas: ")
        lista.extend(respostaifs.split(','))
  
    elif(resposta == 3):
        respostaifs = input("\n\nAdiciona uma tarefa : ")
        num = int(input("Que posicao queres uma tarefa : "))
        lista.insert(num, respostaifs)
        
    elif(resposta == 4):
        respostaifs = input("\n\nQue tarefa queres remover : ")
        lista.remove(respostaifs)
        
    elif(resposta == 5):
        rep = int(input("\n\nQueres remover a ultima tarefa ou alguma em espcifica(1/2) : "))
        if(rep == 2):
            respostaifs = int(input("Qual posicao queres remover : "))
            lista.pop(respostaifs)
        else:
            lista.pop()
            print("\nUltima tarefa eliminada\n\n")
            
    elif(resposta == 6):
        lista.clear()
        print("\nTodas as tarefas foram removidas")
            
    elif(resposta == 7):
        respostaifs = input("Que tarefa pretendes ver : ")
        numTarefas = lista.count(respostaifs)
        print("\nConsseguimos ver a tarefa", respostaifs, numTarefas, "vezes")
        
    elif(resposta == 8):
        print("\nA primeira tarefa da lista é : ", lista[0])
            
    elif(resposta == 9):
        lista.sort()
        print("\nAs tarefas agora estao ordenadas")
        print(lista)
        
    elif(resposta == 10):
        lista.reverse()
        print("\nAgora a lista está invertida")
        print(lista)
        
    elif(resposta == 11):
        lista2 = lista
        print("\nAgora temos a lista 1 e 2")
        print("Lista 1: ",lista, "Lista 2 Copia: ", lista2)
        
        
        
print("Lista final : ",lista)


