#List Comprehension

# nums = []
# for i in range(0, 100):
#     nums.append(i)
    
nums = [i for i in range(0, 100)]

nums2 = [8, 11, 5, 3, 21]

nums_filtrados = []

nums_filtrados2 = []

for num in nums2:
    if 10 <= num <=20:
        if num % 2:
            nums_filtrados2.append(num*2)
        else:
            nums_filtrados2.append(num)

#nums_filtrados = [nums for num in nums2 if 10 <= num <= 20]

nums_filtrados3 = [num*2 if num % 2 == 0 else num for num in nums2 if 10 <= num <=20]

print(nums_filtrados3)


frutas = ["morango", "banana", "ameixa", "pera"]
#N caracteres de cada fruta
letras_frutas = [len(fruta) for fruta in frutas]

print(letras_frutas)