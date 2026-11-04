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
                print(print_product(product))
        case 3:
            for product in products:
                update_final_price(products[0])
                
        case 4:
            resposta = input("Que produto queres que imprima: ")
            print_product(resposta)
            
    #os.system("clear")
    escolha = menu()