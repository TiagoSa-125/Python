def verInventario(inventario):
    if inventario.keys():
        for livro in inventario.values():
            print("\nId: ",livro["id"], " \nDo livro: ", livro["titulo"], " de ", livro["autor"], "\nTem ",
                livro["quantidade"], " em stock e cada unidade custa", livro["preco"])
    else:
        print("Nao tens livros no inventario")

def adicionaItem(titulo, autor, quantidade, preco):
    return {"id": 3, "titulo": titulo, "autor": autor, "quantidade": quantidade, "preco": preco}


def menu():
    print("1- Ver Inventario")
    print("2- Listar os produtos existentes")
    print("3- Atualizar o preço final de todos os produtos existentes na lista")
    print("4- Imprimir os dados de um produto específico")
    print("5- Terminar a aplicação")
    op = input("Escolhe uma opcão : ")
    return op