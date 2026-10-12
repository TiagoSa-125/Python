nums = [2,5,4,7]

print(nums[1]) # 5

#Adicionar um numero
nums.append(15)

#Adicionar Varios numeros
nums.extend([12,23,67])

#Inserir em posições especificas
nums.insert(3, 29)  #Na posição 3 mete 29

#Remover o ultimo numero da lista
nums.pop

#Remover um numero de uma posicçao especifica da lista
nums.pop(3)# Posicao 3

#Remover um numero da lista
nums.remove(2)# Tira o numero 2 nao posiçao tira o numero mesmo

total = len(nums) 
print(total)

print(nums)