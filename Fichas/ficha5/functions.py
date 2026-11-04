
def add(produto, preco, iva):
    return {"product": produto, "price" : preco, "tax" : iva}

def update_final_price(d):
    d["final_price"] = round(d["price"] * (1+d["tax"]), 2)

def print_product(d):
    return "O produto", d,["product"], "com o preco de", d["price"], "e iva de ", (d["tax"]*100)



def menu():
    print("1- Inserir um novo Produto")
    print("2- Listar os produtos existentes")
    print("3- Atualizar o preço final de todos os produtos existentes na lista")
    print("4- Imprimir os dados de um produto específico")
    print("5- Terminar a aplicação")
    op = input("Escolhe uma opcão : ")
    return op
    