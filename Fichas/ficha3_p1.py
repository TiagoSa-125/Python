lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


pares = [num for num in lista if num % 2 == 0]

quadrados = [num * num for num in lista]

print(quadrados)
    
print(pares)


palavras= ["Goncalo", "Batata", "Pipoca"]

paTamanho = [len(tamanho) for tamanho in palavras]

print(paTamanho)


numLista = [20, 15, 2, 1]

maior5num = [num for num in numLista if num > 5]

print(maior5num)

nome = "MarcelO ViEiRaamorIM"

letrasMaiores = [letra for letra in nome if letra]