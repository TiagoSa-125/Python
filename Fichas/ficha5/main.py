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

while (escolha != 5):
    match(escolha):
        case 1:
            ...
        case 2:
            ...
    os.system("clear")
    escolha = menu()