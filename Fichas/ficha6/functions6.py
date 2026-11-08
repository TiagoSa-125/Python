def verInventario(inventario):
    if inventario.keys():
        for livro in inventario.values():
            print("\nId: ",livro["id"], " \nDo livro: ", livro["titulo"], " de ", livro["autor"], "\nTem ",
                livro["quantidade"], " em stock e cada unidade custa", livro["preco"])
    else:
        print("Nao tens livros no inventario")

def adicionaItem(titulo, autor, quantidade, preco):
    return {"id": 3, "titulo": titulo, "autor": autor, "quantidade": quantidade, "preco": preco}
