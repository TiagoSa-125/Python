def saudacao(nome, curso):
    print("Bem vindo ao curso de ", curso, nome)
    
saudacao("Roberto", "Programação")



# hoteis = "67"

# def funcao():
#     global hoteis
#     print(hoteis)
    
# funcao()


# def criar_lista(*alunos):
#     # *alunos significa que vai receber varios parametros
#     lista = []
#     for aluno in alunos:
#         lista.append(aluno)
#     return lista


# x = criar_lista("Ana", "Joao")
# y = criar_lista("Rui", "Maria", "Felix")
# z = ["A1", "A2"]

# nova_lista = criar_lista(*z)
#  # o *z significa que vai tirar os valores da lista z e meter na nova lista para que nao meta uma lista dentro de outra

# print(x, y, nova_lista)
    
    
def config(**configuracoes):
    for chave, valor in configuracoes.items():
        print(chave, "=", valor)
    
config(memoria="16GB", disco="SSD 256GB", sistema = "Windows 11")

dicionario = {"memoria": "8GB", "disco": "SSD 512GB", "sistema" : "Fedora"}

config(**dicionario)

