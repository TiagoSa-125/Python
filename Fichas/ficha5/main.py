from functions import add, update_final_price, print_product, menu
import os

products = []

# products.append(add("camisa", 12.23, 0.13))

# prd = input("Digite o nome do produto: ")
# pri = float(input("Digite o preco do produto: "))
# iva = float(input("Iva do produto: "))

# products.append(add(prd, pri, iva))
# update_final_price(products[0])
# print(products)

# for product in products:
#     print(print_product(products))
    
escolha = menu()

while True:
    match(escolha):
        case 1:
            prd = input("Digite o nome do produto: ")
            pri = float(input("Digite o preço do produto: "))
            iva = float(input("Iva do produto: "))
            products.append(add(prd,pri,iva))
        case 2:
            for product in products:
                if "final_price" not in product.keys():
                    update_final_price(product)
                print(print_product(product))
                x = input("Prima uma tecla para continuar")
        case 3:
            for product in products:
                update_final_price(products)
                
        case 4:
            encontrei = False
            resposta = input("Que produto queres que imprima: ")
            for p in products:
                if p["product"] == resposta:
                    print(print_product(p))
                    encontrei = True
            if not encontrei:
                print("Este produto nao faz parte da lista")
            x = input("Prima uma tecla para continuar")
        case 5:
            break            
            
    #os.system("clear")
    escolha = menu()