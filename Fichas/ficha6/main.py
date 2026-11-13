from functions6 import verInventario, adicionaItem, menu

Inventario = {
    "livro1" : {
        "id": 1 ,
        "titulo": "Gato Gordo" ,
        "autor": "Goncalo Serra" ,
        "quantidade": 3 ,
        "preco": 12.99
        
    },
    "livro2" : {
        "id": 2 ,
        "titulo": "Gato Preto" ,
        "autor": "Giovani Trindade" ,
        "quantidade": 4 ,
        "preco": 137.67
        
    }
}
inventario_total = [livro for livro in Inventario.values()]
# for livro in Inventario.values():
#     inventario_total.append(livro)

#print(inventario_total)




while True:
    escolha = menu()
    match(escolha):
        case "1":
            verInventario(Inventario)
        case "2":
                for livro in Inventario.values():
                    id = livro["id"] + 1
                    
                titulo = input("Qual o titulo do livro: ")
                autor = input("Qual o autor do livro: ")
                quantidade = int(input("Quantas unidades tem: "))
                preco = float(input("Qual o preco do livro: "))

                Inventario["livro3"] =adicionaItem(id, titulo, autor, quantidade, preco)
        case "3":
            
        case "5":
            break   

