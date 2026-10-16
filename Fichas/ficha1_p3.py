from random import randint 

numeroSecreto = randint(1,100)

jogAgain = "S"

numTentivas =int(7)

ganhou = False

print(numeroSecreto)

pontos = [100, 80, 60, 40, 30, 20, 10]

contapontos = 0

while jogAgain == "S":

    print("\nTens ", numTentivas, " tentativas restantes")
    resposta = int(input("Diz um numero: "))
        
    if(resposta < 1 or resposta > 100):
        print("\n\nNumero invalido tem de ser maior que 0 e menor que 100")
        
        
    elif(resposta == numeroSecreto):
        print("\n\nParabens ganhaste ")
        ganhou = True
            
    elif(resposta > numeroSecreto):
        print("\n\nO teu numero :", resposta, " é maior que o numero secreto")
        numTentivas = numTentivas - 1
        contapontos = contapontos + 1
    else:
        print("\n\nO teu numero :", resposta, " é menor que o numero secreto")
        numTentivas = numTentivas + 1
        contapontos = contapontos + 1
        
        
    if(numTentivas == 0):
        print("Perdeste :(  o numero era: ", numeroSecreto)
        jogAgain = input("\nQueres jogar de novo ?(S/N): ")  
        numTentivas = 7
        numeroSecreto = randint(1,100)
            
    elif(ganhou == True):
        print("Ganhaste :) Acabaste com ", pontos[contapontos])
        jogAgain = input("\nQueres jogar de novo ?(S/N): ")
        numTentivas = 7
        ganhou = False
        numeroSecreto = randint(1,100)
            
        





