texto = "Tiago Sa"

contagem = {}

for letra in texto:
    letra = letra.lower()
    if letra in contagem.keys():
        contagem [letra] += 1
    else:
        contagem[letra] =  1
        
print(contagem)