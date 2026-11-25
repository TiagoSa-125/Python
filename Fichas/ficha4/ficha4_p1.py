aluno = {
    "nome":"Ana Silva", "idade": 17, "disciplinas": ["Matemática", "Física", "Informática"] , 
    "notas": {"Matemática": 18, "Física": 17, "Informática": 19}
}

#Ex 1
aluno["disciplinas"].append("Portugues")
aluno["notas"]["Português"] = 16

print(aluno["disciplinas"], aluno["notas"])

#Ex 2
aluno["idade"] = 18


#Ex 3
print("\n\nNotas : \n", aluno["notas"])

#Ex 4

soma = sum(aluno['notas'].values())

num_notas = len(aluno['notas'])

media = round(soma / num_notas, 2)

print('\n\nA media das notas dá:', media)
    


