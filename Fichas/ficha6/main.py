Inventario = {
    "livro" : {
        "id": 1 ,
        "titulo": "Gato Gordo" ,
        "autor": "Goncalo Serra" ,
        "quantidade": 3 ,
        "preco": 12.99
        
    }
}


inventario_total = [livro for livro in Inventario["livro"].values()]
print(inventario_total)


