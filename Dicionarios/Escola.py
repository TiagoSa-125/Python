escola = {
    "aluno1": {
        "nome": "Ana Silva",
        "idade": 17,
        "cidade": "Porto",
        "curso": "Programador",
        "notas": {
            "Python": 18,
            "Excel": 16,
            "SQL": 15
        },
        "contacto": {
            "email": "ana@email.com",
            "telefone": "912345678"
        }
    },

    "aluno2": {
        "nome": "João Costa",
        "idade": 18,
        "cidade": "Braga",
        "curso": "Programador",
        "notas": {
            "Python": 14,
            "Excel": 17,
            "SQL": 16
        },
        "contacto": {
            "email": "joao@email.com",
            "telefone": "923456789"
        }
    },

    "aluno3": {
        "nome": "Maria Santos",
        "idade": 16,
        "cidade": "Aveiro",
        "curso": "Programador",
        "notas": {
            "Python": 19,
            "Excel": 18,
            "SQL": 20,
            "Extra": 16
        },
        "contacto": {
            "email": "maria@email.com",
            "telefone": "934567890"
        }
    }
}


# medi_idade_alunos = 0.0
# somaIdades = 0
# for aluno in escola.values():
#     somaIdades += aluno["idade"]
    
# medi_idade_alunos = round(somaIdades / len(escola), 2)
# print(medi_idade_alunos)


#Imprime o nome do aluno e a media das notas

for aluno in escola.values():
    nome_aluno = aluno["nome"]
    notas_aluno = []
    
    for notas in aluno["notas"].values():
        notas_aluno.append(notas)
        
    media = round (sum(notas_aluno)/len(notas_aluno),2)
    print("O aluno ", nome_aluno, "teve media de ", media)
    
# Aluno do Porto
escola_porto = {}
for chave, valor in escola.items():
    if valor["cidade"] == "Porto":
        escola_porto[chave] = valor

print(escola_porto)

#Dictionary Comprhension
escola_porto2 = {chave:valor for chave,valor in escola.items() if valor["cidade"] == "Porto"}
print(escola_porto2)