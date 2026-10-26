aluno = {"nome": "Carlos", "idade": 17, "cidade"  : "Famalicao"
         , "disciplinas": ["Matemática", "Programação", "Ingles"]
         , "notas" : {"matematica" : [17.5], "programacao" : [18.25, 13], "ingles": [12.25]}}

#Media de todas as notas
soma = 0
num_notas = 0
for notas_disciplina in aluno["notas"].values():
    soma += sum(notas_disciplina)
    no_notas += len[notas_disciplina]




print(aluno["notas"]["programacao"][1])

#print(aluno["nome"])

#Alterar valor de uma chave

aluno["idade"] = 18

#Inserir uma nova chave
aluno["estado_civil"] = "Solteiro"

#print(aluno)

#Imprimir as caracteristicas do aluno

for chave in aluno.keys():
    print(chave, end=" ")
    
#Imprimir só os valores

for valor in aluno.values():
    print("\n",valor, end=" ")

print("\n\n")
#Imprimir a chave e o valor 
for chave, valor in aluno.items():
    print(chave, valor)
    
    
print(aluno["disciplinas"])

#Como adicionar numa lista de um dicionario
aluno["disciplinas"].append("Portugues")

print(aluno["disciplinas"])
