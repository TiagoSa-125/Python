#Ex 1
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


pares = [num for num in lista if num % 2 == 0]
print(pares)

#Ex 2
quadrados = [num * num for num in lista]
print(quadrados)

    

#Ex 3

palavras= ["Goncalo", "Batata", "Pipoca"]

paTamanho = [len(tamanho) for tamanho in palavras]

print(paTamanho)


#Ex 4

numLista = [20, 15, 2, 1]

maior5num = [num for num in numLista if num > 5]

print(maior5num)



#Ex 5

nome = "MarcelO ViEiRaamorIM"

letrasMaiores = [letra for letra in nome if letra.lower() != letra]

print(letrasMaiores)


#Ex 6

numsLista = [2, 3, 6, 9, 15, 22, 1]
numsLista2 = [num*2 if num % 3 == 0 else num for num in numsLista]

print(numsLista2)


#Ex 7
nomeLista = ["Giovani", "Ana", "Goncalo", "Artur"]
nomeLista2 = [nome.upper() for nome in nomeLista if nome.startswith("A") ]

print(nomeLista2)



#Ex 8

listaFruta = ["Maca", "Pera", "Laranja", "Maracuja"]
tamanhoFruta = [len(fruta) if len(fruta) > 5 else 0 for fruta in listaFruta]

print(tamanhoFruta)

