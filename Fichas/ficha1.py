from random import randint

lista = []
pares = 0
impares = 0



for _ in range(30):
    x = randint(1,100)
    lista.append(x)
    
    if (x % 2 == 0):
        pares = pares + 1
    else:
        impares = impares +1
        
soma = sum(lista)
maior = max(lista)
menor = min(lista) 
media = soma/ len(lista)

contaMedia = 0
nums_acima_media = []

for x in lista:
    if(x > media):
        contaMedia = contaMedia + 1
        nums_acima_media.append(x)
    
    
print("Lista : ", lista)

print("Numero de pares que temos :", pares)  

print("Numero de impares que temos :", impares)  

print("O maior numero : ", maior)  

print("O menor numero : ", menor)  

print("A media dos numeros : ", round(media, 2))  

print("Numero de numeros maiores que a media : ", contaMedia)  

print("Numeros maiores que a media : ", nums_acima_media)  
    

    
