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

for livro in biblioteca:
    if livro["disponivel"]:
        print("Sim")
    else:
        print("Não")
