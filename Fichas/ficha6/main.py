from functions6 import verInventario

Inventario = {
    # "livro1" : {
    #     "id": 1 ,
    #     "titulo": "Gato Gordo" ,
    #     "autor": "Goncalo Serra" ,
    #     "quantidade": 3 ,
    #     "preco": 12.99
        
    # },
    # "livro2" : {
    #     "id": 2 ,
    #     "titulo": "Gato Preto" ,
    #     "autor": "Giovani Trindade" ,
    #     "quantidade": 4 ,
    #     "preco": 137.67
        
    # }
}
inventario_total = [livro for livro in Inventario.values()]
# for livro in Inventario.values():
#     inventario_total.append(livro)

#print(inventario_total)

verInventario(Inventario)
