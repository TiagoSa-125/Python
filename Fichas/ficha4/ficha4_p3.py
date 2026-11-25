biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}

#Ex 2

# titulo = input("Qual o titulo do livro: ")
# autor = input("Qual o autor do livro: ")
# ano = input("Qual o ano do livro: ")
# disponivel = input("O livro esta disponivel: (s/n) ")

# if disponivel.lower() == "s":
#     disponivel = True
# else:
#     disponivel = False
    
# biblioteca["livro4"]= {
#     "titulo": titulo,
#     "autor": autor,
#     "ano": ano,
#     "disponivel": disponivel

# }

# print(biblioteca)


#Ex 3

# biblioteca["livro1"]["disponivel"] = False

# print(biblioteca)


lista = []

for livro in biblioteca:
    if biblioteca[livro]["autor"] == "Luciano Ramalho":
        lista.append(biblioteca[livro]["titulo"])
        
print(lista)