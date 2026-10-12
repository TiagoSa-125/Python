from random import randint


notas = []

numAlunos = 15
alunos_aprovados = 0
alunos_reprovados = 0
notas_superiores_16 = 0


for _ in range(15):
    x = randint(0,20)
    notas.append(x)
    
  
soma = sum(notas)
maior = max(notas)
menor = min(notas) 
media = soma/ len(notas)

  
for x in notas:
    if(x >= 10):
        alunos_aprovados = alunos_aprovados + 1
    else:
        alunos_reprovados = alunos_reprovados +1
        
    if(x >= 16):
            notas_superiores_16 = notas_superiores_16 + 1
    
    
percentagemAprova = (alunos_aprovados/numAlunos)*100

print("A maior nota : ", maior)
print("A menor nota : ", menor)
print("A media da turma : ", round(media, 2 ))
print("A percentagem de aprovacao da turma: ", percentagemAprova, "%")
