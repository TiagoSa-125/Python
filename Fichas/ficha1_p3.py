from random import randint 

numeroSecreto = randint(1,100)

jogAgain = "S"

numTentivas =int(7)

ganhou = False

# print(numeroSecreto)


while jogAgain.upper == "S":

    print("\nTens ", numTentivas, " tentativas restantes")
    resposta = int(input("Diz um numero: "))
        
    if(resposta < 1 or resposta > 100):
        print("\n\nNumero invalido tem de ser maior que 0 e menor que 100")
        ganhou = True
        
    elif(resposta == numeroSecreto):
        print("\n\nParabens ganhaste ")
            
    elif(resposta > numeroSecreto):
        print("\n\nO teu numero :", resposta, " é maior que o numero secreto")
        numTentivas = numTentivas - 1
    else:
        print("\n\nO teu numero :", resposta, " é menor que o numero secreto")
        numTentivas = numTentivas - 1
        
    if(numTentivas == 0):
        jogAgain = input("Perdeste :( \nQueres jogar de novo ?(S/N): ")
          
            
    if(ganhou == True):
        jogAgain = input("Ganhaste :) \nQueres jogar de novo ?(S/N): ")
            
        





