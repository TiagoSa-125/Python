def verInventario(inventario):
    if inventario.keys():
        for livro in inventario.values():
            print("\nId: ",livro["id"], " \nDo livro: ", livro["titulo"], " de ", livro["autor"], "\nTem ",
                livro["quantidade"], " em stock e cada unidade custa", livro["preco"])
    else:
        print("Nao tens livros no inventario")